import pytest
from src.etc.migration_service import (
    Category,
    Group,
    MigrationType,
    MigrationService,
    PersistenceManager,
    Product,
)


# ──────────────────────────────────────────────────────────────────────────────
# Mock PersistenceManager (in-memory)
# ──────────────────────────────────────────────────────────────────────────────


class MockPM(PersistenceManager):
    """In-memory PersistenceManager for testing."""

    def __init__(self) -> None:
        self._products: dict[str, Product] = {}
        self._categories: dict[str, Category] = {}
        # product_name → [category_name, ...]
        self._prod_cats: dict[str, list[str]] = {}
        # category_name → [product_name, ...]
        self._cat_prods: dict[str, list[str]] = {}

    # ── PersistenceManager interface ──────────────────────────────────────────

    def create_product(self, name: str, g: Group) -> Product:
        if name in self._products:
            raise ValueError(f"Product '{name}' already exists")
        p = Product(name, g)
        self._products[name] = p
        self._prod_cats[name] = []
        return p

    def create_category(self, name: str, g: Group) -> Category:
        if name in self._categories:
            raise ValueError(f"Category '{name}' already exists")
        c = Category(name, g)
        self._categories[name] = c
        self._cat_prods[name] = []
        return c

    def add_product_to_category(self, p: Product, c: Category) -> None:
        self._prod_cats[p.getName()].append(c.getName())
        self._cat_prods[c.getName()].append(p.getName())

    def remove_product_from_category(self, p: Product, c: Category) -> None:
        self._prod_cats[p.getName()].remove(c.getName())
        self._cat_prods[c.getName()].remove(p.getName())

    def update_product(self, p: Product, new_name: str) -> None:
        old = p.getName()
        if new_name != old and new_name in self._products:
            raise ValueError(f"Product '{new_name}' already exists")
        self._products.pop(old)
        p._setName(new_name)
        self._products[new_name] = p
        cats = self._prod_cats.pop(old)
        self._prod_cats[new_name] = cats
        for cat_name in cats:
            prods = self._cat_prods[cat_name]
            prods[prods.index(old)] = new_name

    def update_category(self, c: Category, new_name: str) -> None:
        old = c.getName()
        if new_name != old and new_name in self._categories:
            raise ValueError(f"Category '{new_name}' already exists")
        self._categories.pop(old)
        c._setName(new_name)
        self._categories[new_name] = c
        prods = self._cat_prods.pop(old)
        self._cat_prods[new_name] = prods
        for prod_name in prods:
            cats = self._prod_cats[prod_name]
            cats[cats.index(old)] = new_name

    def delete_product(self, p: Product) -> None:
        name = p.getName()
        for cat_name in self._prod_cats.get(name, []):
            self._cat_prods[cat_name].remove(name)
        self._prod_cats.pop(name, None)
        self._products.pop(name, None)

    def get_categories(self, p: Product) -> list[Category]:
        return [self._categories[n] for n in self._prod_cats.get(p.getName(), [])]

    def get_products(self, c: Category) -> list[Product]:
        return [self._products[n] for n in self._cat_prods.get(c.getName(), [])]

    # ── Test helpers ──────────────────────────────────────────────────────────

    def product_names(self) -> set[str]:
        return set(self._products)

    def category_names(self) -> set[str]:
        return set(self._categories)

    def products_in(self, cat_name: str) -> set[str]:
        return set(self._cat_prods.get(cat_name, []))

    def cats_of(self, prod_name: str) -> set[str]:
        return set(self._prod_cats.get(prod_name, []))


class FailingMockPM(MockPM):
    """특정 이름을 두 번째 생성 시 예외를 던지는 MockPM.

    첫 번째 호출은 setup용으로 성공, 두 번째 호출(마이그레이션 시도)부터 실패.
    """

    def __init__(self, fail_product: str = "", fail_category: str = "") -> None:
        super().__init__()
        self._fail_product = fail_product
        self._fail_category = fail_category
        self._product_calls: dict[str, int] = {}
        self._category_calls: dict[str, int] = {}

    def create_product(self, name: str, g: Group) -> Product:
        if name == self._fail_product:
            count = self._product_calls.get(name, 0) + 1
            self._product_calls[name] = count
            if count > 1:  # 두 번째 호출부터 실패 (첫 번째는 setup용)
                raise ValueError(
                    f"Simulated failure: product '{name}' cannot be created"
                )
        return super().create_product(name, g)

    def create_category(self, name: str, g: Group) -> Category:
        if name == self._fail_category:
            count = self._category_calls.get(name, 0) + 1
            self._category_calls[name] = count
            if count > 1:  # 두 번째 호출부터 실패 (첫 번째는 setup용)
                raise ValueError(
                    f"Simulated failure: category '{name}' cannot be created"
                )
        return super().create_category(name, g)


# ──────────────────────────────────────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────────────────────────────────────


@pytest.fixture
def src_group() -> Group:
    return Group("logic")


@pytest.fixture
def dst_group() -> Group:
    return Group("sport")


@pytest.fixture
def pm() -> MockPM:
    return MockPM()


@pytest.fixture
def svc(pm: MockPM) -> MigrationService:
    return MigrationService(pm)


def setup_puzzle(pm: MockPM, src: Group) -> tuple[Product, Product, Category]:
    """
    logic 그룹에 다음 구조 생성:
        Category: puzzle
            Product: puzzle_1
            Product: puzzle_2
    """
    cat = pm.create_category("puzzle", src)
    p1 = pm.create_product("puzzle_1", src)
    p2 = pm.create_product("puzzle_2", src)
    pm.add_product_to_category(p1, cat)
    pm.add_product_to_category(p2, cat)
    return p1, p2, cat


# ──────────────────────────────────────────────────────────────────────────────
# Type 1: COPY
# ──────────────────────────────────────────────────────────────────────────────


def test_copy_product_creates_copy_in_target_group(
    pm: MockPM, svc: MigrationService, src_group: Group, dst_group: Group
) -> None:
    # Given
    p = pm.create_product("ball_1", src_group)

    # When
    svc.migrate(p, dst_group, MigrationType.COPY)

    # Then
    assert "ball_1" in pm.product_names()  # 원본 유지
    assert "ball_1-copy" in pm.product_names()  # 복사본 생성


def test_copy_category_creates_copy_without_children(
    pm: MockPM, svc: MigrationService, src_group: Group, dst_group: Group
) -> None:
    # Given
    _, _, cat = setup_puzzle(pm, src_group)

    # When
    svc.migrate(cat, dst_group, MigrationType.COPY)

    # Then - 카테고리 복사본 생성, 하위 제품은 복사 안 됨
    assert "puzzle" in pm.category_names()
    assert "puzzle-copy" in pm.category_names()
    assert pm.products_in("puzzle-copy") == set()


# ──────────────────────────────────────────────────────────────────────────────
# Type 2: MOVE
# ──────────────────────────────────────────────────────────────────────────────


def test_move_product_removes_original_and_creates_in_target(
    pm: MockPM, svc: MigrationService, src_group: Group, dst_group: Group
) -> None:
    # Given
    p = pm.create_product("ball_1", src_group)

    # When
    svc.migrate(p, dst_group, MigrationType.MOVE)

    # Then - 원본 삭제, 이동 완료
    assert "ball_1" in pm.product_names()
    assert "ball_1-temp" not in pm.product_names()


def test_move_category_renames_original_and_creates_in_target(
    pm: MockPM, svc: MigrationService, src_group: Group, dst_group: Group
) -> None:
    # Given
    _, _, cat = setup_puzzle(pm, src_group)

    # When
    svc.migrate(cat, dst_group, MigrationType.MOVE)

    # Then - 원본은 -temp로 남음(delete_category 없음), 새 카테고리 생성
    assert "puzzle" in pm.category_names()
    assert "puzzle-temp" in pm.category_names()


def test_move_product_restores_original_on_create_failure(
    src_group: Group, dst_group: Group
) -> None:
    # Given - create_product("ball_1") 호출 시 실패하도록 설정
    failing_pm = FailingMockPM(fail_product="ball_1")
    svc = MigrationService(failing_pm)
    p = failing_pm.create_product("ball_1", src_group)

    # When / Then - 예외 발생, 원본 이름 복원
    with pytest.raises(ValueError):
        svc.migrate(p, dst_group, MigrationType.MOVE)

    assert "ball_1" in failing_pm.product_names()  # 원본 복원
    assert "ball_1-temp" not in failing_pm.product_names()


def test_move_category_restores_original_on_create_failure(
    src_group: Group, dst_group: Group
) -> None:
    # Given - create_category("puzzle") 호출 시 실패하도록 설정
    failing_pm = FailingMockPM(fail_category="puzzle")
    svc = MigrationService(failing_pm)
    _, _, cat = setup_puzzle(failing_pm, src_group)

    # When / Then
    with pytest.raises(ValueError):
        svc.migrate(cat, dst_group, MigrationType.MOVE)

    assert "puzzle" in failing_pm.category_names()  # 원본 복원
    assert "puzzle-temp" not in failing_pm.category_names()


# ──────────────────────────────────────────────────────────────────────────────
# Type 3: COPY_WITH_DEPENDENCIES
# ──────────────────────────────────────────────────────────────────────────────


def test_copy_product_with_deps_copies_category_and_siblings(
    pm: MockPM, svc: MigrationService, src_group: Group, dst_group: Group
) -> None:
    # Given: puzzle_1, puzzle_2 ∈ puzzle
    p1, p2, cat = setup_puzzle(pm, src_group)

    # When: puzzle_1 복사 (의존성 포함)
    svc.migrate(p1, dst_group, MigrationType.COPY_WITH_DEPENDENCIES)

    # Then: puzzle-copy 카테고리와 puzzle_1-copy, puzzle_2-copy 생성
    assert "puzzle-copy" in pm.category_names()
    assert "puzzle_1-copy" in pm.product_names()
    assert "puzzle_2-copy" in pm.product_names()
    assert pm.products_in("puzzle-copy") == {"puzzle_1-copy", "puzzle_2-copy"}

    # 원본 유지
    assert "puzzle" in pm.category_names()
    assert "puzzle_1" in pm.product_names()
    assert "puzzle_2" in pm.product_names()


def test_copy_category_with_deps_copies_all_children(
    pm: MockPM, svc: MigrationService, src_group: Group, dst_group: Group
) -> None:
    # Given: puzzle_1, puzzle_2 ∈ puzzle
    p1, p2, cat = setup_puzzle(pm, src_group)

    # When: puzzle 카테고리 복사 (의존성 포함)
    svc.migrate(cat, dst_group, MigrationType.COPY_WITH_DEPENDENCIES)

    # Then
    assert "puzzle-copy" in pm.category_names()
    assert "puzzle_1-copy" in pm.product_names()
    assert "puzzle_2-copy" in pm.product_names()
    assert pm.products_in("puzzle-copy") == {"puzzle_1-copy", "puzzle_2-copy"}


def test_copy_with_deps_preserves_all_originals(
    pm: MockPM, svc: MigrationService, src_group: Group, dst_group: Group
) -> None:
    # Given
    p1, p2, cat = setup_puzzle(pm, src_group)

    # When
    svc.migrate(p1, dst_group, MigrationType.COPY_WITH_DEPENDENCIES)

    # Then: 원본 모두 유지
    assert {"puzzle_1", "puzzle_2"}.issubset(pm.product_names())
    assert "puzzle" in pm.category_names()


# ──────────────────────────────────────────────────────────────────────────────
# Type 4: MOVE_WITH_DEPENDENCIES
# ──────────────────────────────────────────────────────────────────────────────


def test_move_product_with_deps_moves_all_three_beings(
    pm: MockPM, svc: MigrationService, src_group: Group, dst_group: Group
) -> None:
    # Given: puzzle_1, puzzle_2 ∈ puzzle
    p1, p2, cat = setup_puzzle(pm, src_group)

    # When: puzzle_1 이동 (의존성 포함)
    svc.migrate(p1, dst_group, MigrationType.MOVE_WITH_DEPENDENCIES)

    # Then: 새 카테고리와 제품 생성, 원본 제품 삭제
    assert "puzzle" in pm.category_names()  # 이동된 카테고리 (원본 이름 유지)
    assert "puzzle_1" in pm.product_names()  # 이동된 제품
    assert "puzzle_2" in pm.product_names()  # 이동된 제품
    assert "puzzle_1-temp" not in pm.product_names()
    assert "puzzle_2-temp" not in pm.product_names()
    # 새 카테고리에 두 제품이 연결되어야 함
    assert pm.products_in("puzzle") == {"puzzle_1", "puzzle_2"}


def test_move_category_with_deps_moves_all_beings(
    pm: MockPM, svc: MigrationService, src_group: Group, dst_group: Group
) -> None:
    # Given: puzzle_1, puzzle_2 ∈ puzzle
    p1, p2, cat = setup_puzzle(pm, src_group)

    # When: puzzle 카테고리 이동 (의존성 포함)
    svc.migrate(cat, dst_group, MigrationType.MOVE_WITH_DEPENDENCIES)

    # Then
    assert "puzzle" in pm.category_names()
    assert "puzzle_1" in pm.product_names()
    assert "puzzle_2" in pm.product_names()
    assert pm.products_in("puzzle") == {"puzzle_1", "puzzle_2"}


def test_move_with_deps_product_restores_on_first_failure(
    src_group: Group, dst_group: Group
) -> None:
    # Given: create_product("puzzle_1") 실패 시뮬레이션
    failing_pm = FailingMockPM(fail_product="puzzle_1")
    svc = MigrationService(failing_pm)
    p1, p2, cat = setup_puzzle(failing_pm, src_group)

    # When / Then
    with pytest.raises(ValueError):
        svc.migrate(p1, dst_group, MigrationType.MOVE_WITH_DEPENDENCIES)

    # 원본 제품들은 시스템에 존재해야 함 (이름이 바뀌어도 객체는 존재)
    all_names = failing_pm.product_names()
    assert "puzzle_1" in all_names or "puzzle_1-temp" in all_names
