"""
Happy Time Inc. - Migration Service

---

Problem Statement:
    You're asked by the company Happy Time Inc. to help them with the migration
    of the products in their system.

Company's System:
    - Product  : a class representing a single product (e.g. puzzle_1, puzzle_2, ball_1)
    - Category : a class representing a product category (e.g. puzzle, balls)
    - Being    : an interface implemented by Product and Category; provides getName()
    - Group    : a new class representing groups of products and categories (e.g. logic, sport)
    - PersistenceManager: the persistence layer with the following methods:
        create_category(name, g)            -> Category
        create_product(name, g)             -> Product
        add_product_to_category(p, c)       -> None
        remove_product_from_category(p, c)  -> None
        update_product(p, newName)          -> None
        update_category(c, newName)         -> None
        delete_product(p)                   -> None
        get_categories(p)                   -> List[Category]
        get_products(c)                     -> List[Product]

Requirements:
    Implement MigrationService.migrate(being, group, migration_type) where
    migration_type is one of:
        1. COPY                   - Copy the specified Being to the desired Group
        2. MOVE                   - Move the specified Being to the desired Group
        3. COPY_WITH_DEPENDENCIES - Copy Being + all related beings
                                    (e.g. copying puzzle_1, which belongs to puzzle
                                    category that also contains puzzle_2, should copy
                                    all three beings; same applies to copying a category)
        4. MOVE_WITH_DEPENDENCIES - Move Being + all related beings
                                    (e.g. moving puzzle_1 moves puzzle_1, puzzle category,
                                    and puzzle_2; same applies to moving a category)

Assumptions:
    - Being names must be unique; creating a duplicate name throws an exception.
    - When creating a copy of a being, add the "-copy" suffix to its name.
    - Only PersistenceManager methods may be used (constructors are not available).
    - Handle exceptions from create_category / create_product.
    - In case of persistence problems, original beings must not be lost.

Key Design:
    - MOVE uses rename-then-create-then-delete pattern for safety:
        1. Rename original → "-temp"  (free up the name)
        2. Try create in target group with original name
        3. On failure → restore original name (no data loss)
        4. On success → delete original (product only; no delete_category available)
"""

from abc import ABC, abstractmethod
from enum import Enum


# ──────────────────────────────────────────────────────────────────────────────
# Domain classes
# ──────────────────────────────────────────────────────────────────────────────


class Being(ABC):
    @abstractmethod
    def getName(self) -> str: ...


class Group:
    def __init__(self, name: str):
        self._name = name

    def getName(self) -> str:
        return self._name


class Product(Being):
    def __init__(self, name: str, group: Group):
        self._name = name
        self._group = group

    def getName(self) -> str:
        return self._name

    def _setName(self, name: str) -> None:
        self._name = name


class Category(Being):
    def __init__(self, name: str, group: Group):
        self._name = name
        self._group = group

    def getName(self) -> str:
        return self._name

    def _setName(self, name: str) -> None:
        self._name = name


# ──────────────────────────────────────────────────────────────────────────────
# PersistenceManager interface
# ──────────────────────────────────────────────────────────────────────────────


class PersistenceManager(ABC):
    @abstractmethod
    def create_category(self, name: str, g: Group) -> Category: ...

    @abstractmethod
    def create_product(self, name: str, g: Group) -> Product: ...

    @abstractmethod
    def add_product_to_category(self, p: Product, c: Category) -> None: ...

    @abstractmethod
    def remove_product_from_category(self, p: Product, c: Category) -> None: ...

    @abstractmethod
    def update_product(self, p: Product, new_name: str) -> None: ...

    @abstractmethod
    def update_category(self, c: Category, new_name: str) -> None: ...

    @abstractmethod
    def delete_product(self, p: Product) -> None: ...

    @abstractmethod
    def get_categories(self, p: Product) -> list[Category]: ...

    @abstractmethod
    def get_products(self, c: Category) -> list[Product]: ...


# ──────────────────────────────────────────────────────────────────────────────
# MigrationType enum
# ──────────────────────────────────────────────────────────────────────────────


class MigrationType(Enum):
    COPY = 1
    MOVE = 2
    COPY_WITH_DEPENDENCIES = 3
    MOVE_WITH_DEPENDENCIES = 4


# ──────────────────────────────────────────────────────────────────────────────
# MigrationService
# ──────────────────────────────────────────────────────────────────────────────


class MigrationService:
    def __init__(self, pm: PersistenceManager):
        self.pm = pm

    def migrate(
        self, being: Being, group: Group, migration_type: MigrationType
    ) -> None:
        if migration_type == MigrationType.COPY:
            self._copy(being, group)
        elif migration_type == MigrationType.MOVE:
            self._move(being, group)
        elif migration_type == MigrationType.COPY_WITH_DEPENDENCIES:
            self._copy_with_deps(being, group)
        elif migration_type == MigrationType.MOVE_WITH_DEPENDENCIES:
            self._move_with_deps(being, group)

    # ── Type 1: Copy (without dependencies) ───────────────────────────────────

    def _copy(self, being: Being, group: Group) -> None:
        if isinstance(being, Product):
            self._copy_product(being, group)
        elif isinstance(being, Category):
            self._copy_category(being, group)

    def _copy_product(self, product: Product, group: Group) -> Product:
        copy_name = product.getName() + "-copy"
        print(f"[COPY] product '{product.getName()}' -> '{copy_name}'")
        return self.pm.create_product(copy_name, group)

    def _copy_category(self, category: Category, group: Group) -> Category:
        copy_name = category.getName() + "-copy"
        print(f"[COPY] category '{category.getName()}' -> '{copy_name}'")
        return self.pm.create_category(copy_name, group)

    # ── Type 2: Move (without dependencies) ───────────────────────────────────

    def _move(self, being: Being, group: Group) -> None:
        if isinstance(being, Product):
            self._move_product(being, group)
        elif isinstance(being, Category):
            self._move_category(being, group)

    def _move_product(self, product: Product, group: Group) -> Product:
        original_name = product.getName()
        temp_name = original_name + "-temp"

        # Step 1: rename → free up the original name
        print(f"[MOVE] product '{original_name}': rename to '{temp_name}'")
        self.pm.update_product(product, temp_name)

        try:
            # Step 2: create with original name in target group
            print(f"[MOVE] product: create '{original_name}' in target group")
            new_product = self.pm.create_product(original_name, group)
        except Exception as e:
            # Step 3 (failure): restore original name → no data loss
            print(f"[MOVE] product: create failed ({e}). Restoring '{original_name}'.")
            self.pm.update_product(product, original_name)
            raise

        # Step 4 (success): delete the temp-named original
        print(f"[MOVE] product: delete original '{temp_name}'")
        self.pm.delete_product(product)
        return new_product

    def _move_category(self, category: Category, group: Group) -> Category:
        original_name = category.getName()
        temp_name = original_name + "-temp"

        # Step 1: rename → free up the original name
        print(f"[MOVE] category '{original_name}': rename to '{temp_name}'")
        self.pm.update_category(category, temp_name)

        try:
            # Step 2: create with original name in target group
            print(f"[MOVE] category: create '{original_name}' in target group")
            new_category = self.pm.create_category(original_name, group)
        except Exception as e:
            # Step 3 (failure): restore original name → no data loss
            print(f"[MOVE] category: create failed ({e}). Restoring '{original_name}'.")
            self.pm.update_category(category, original_name)
            raise

        # Note: delete_category is not available; old category remains as temp-named
        return new_category

    # ── Type 3: Copy with dependencies ────────────────────────────────────────

    def _copy_with_deps(self, being: Being, group: Group) -> None:
        if isinstance(being, Product):
            self._copy_product_with_deps(being, group)
        elif isinstance(being, Category):
            self._copy_category_with_deps(being, group)

    def _copy_product_with_deps(self, product: Product, group: Group) -> None:
        """
        puzzle_1 복사 예시:
            puzzle_1 → puzzle_1-copy
            puzzle   → puzzle-copy
            puzzle_2 → puzzle_2-copy  (puzzle의 형제 제품)
        """
        categories = self.pm.get_categories(product)
        for category in categories:
            new_category = self._copy_category(category, group)
            for sibling in self.pm.get_products(category):
                new_prod = self._copy_product(sibling, group)
                self.pm.add_product_to_category(new_prod, new_category)

    def _copy_category_with_deps(self, category: Category, group: Group) -> None:
        """
        puzzle 복사 예시:
            puzzle   → puzzle-copy
            puzzle_1 → puzzle_1-copy
            puzzle_2 → puzzle_2-copy
        """
        new_category = self._copy_category(category, group)
        for prod in self.pm.get_products(category):
            new_prod = self._copy_product(prod, group)
            self.pm.add_product_to_category(new_prod, new_category)

    # ── Type 4: Move with dependencies ────────────────────────────────────────

    def _move_with_deps(self, being: Being, group: Group) -> None:
        if isinstance(being, Product):
            self._move_product_with_deps(being, group)
        elif isinstance(being, Category):
            self._move_category_with_deps(being, group)

    def _move_product_with_deps(self, product: Product, group: Group) -> None:
        """
        puzzle_1 이동 예시:
            puzzle_1, puzzle, puzzle_2 모두 target group으로 이동
        """
        categories = self.pm.get_categories(product)
        for category in categories:
            # 이동 전에 제품 목록 먼저 확보 (이동 중 목록 변경 방지)
            siblings = self.pm.get_products(category)
            new_category = self._move_category(category, group)
            for sibling in siblings:
                new_prod = self._move_product(sibling, group)
                self.pm.add_product_to_category(new_prod, new_category)

    def _move_category_with_deps(self, category: Category, group: Group) -> None:
        """
        puzzle 이동 예시:
            puzzle, puzzle_1, puzzle_2 모두 target group으로 이동
        """
        products = self.pm.get_products(category)  # 이동 전에 먼저 확보
        new_category = self._move_category(category, group)
        for prod in products:
            new_prod = self._move_product(prod, group)
            self.pm.add_product_to_category(new_prod, new_category)
