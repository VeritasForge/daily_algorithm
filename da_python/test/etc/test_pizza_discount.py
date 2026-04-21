"""
Tests for pizza_discount.py

각 할인 시나리오와 엣지 케이스를 독립적으로 검증한다.
"""

import pytest

from src.etc.pizza_discount import OrderItem, Pizza, solution

pytestmark = pytest.mark.skip(reason="WIP")


# ── Discount 1: Buy 3, cheapest one is free ─────────────────────────────────


@pytest.mark.parametrize(
    "menu, order, expected",
    [
        # 기본 예제: texas Medium(9) + european Small×2(5,5) → 19 - 5 = 14
        (
            [
                Pizza("greek", 7, 5, 10),
                Pizza("texas", 8, 9, 13),
                Pizza("european", 5, 5, 13),
            ],
            [
                OrderItem("texas", "Medium", 1),
                OrderItem("european", "Small", 2),
            ],
            14,
        ),
        # 정확히 3개 경계값
        (
            [Pizza("a", 10, 15, 20), Pizza("b", 5, 8, 12)],
            [
                OrderItem("a", "Small", 1),
                OrderItem("b", "Small", 1),
                OrderItem("b", "Medium", 1),
            ],
            # base=10+5+8=23, cheapest=5 → 18
            18,
        ),
        # Large가 Small보다 저렴한 경우 (cheapest = Large)
        (
            [Pizza("boston", 7, 5, 3)],
            [OrderItem("boston", "Large", 3)],
            # base=9, cheapest=3 → 6
            6,
        ),
    ],
)
def test_discount1_buy3_cheapest_free(menu, order, expected):
    assert solution(menu, order) == expected


# ── Discount 2: Buy 5 of same name for 100 ──────────────────────────────────


@pytest.mark.parametrize(
    "menu, order, expected",
    [
        # 기본 예제: margherita 5개(90×4 + 80) = 440 → 100, 나머지 정상가
        # greek Small×5(50), hawaii Large×1(120), capricciosa Small×7(50)
        # base = 250 + 360 + 160 + 120 + 350 = 1240
        # best D2 savings = 440 - 100 = 340 → 900
        (
            [
                Pizza("greek", 50, 60, 70),
                Pizza("margherita", 90, 80, 100),
                Pizza("hawaii", 80, 90, 120),
                Pizza("capricciosa", 50, 70, 130),
            ],
            [
                OrderItem("greek", "Small", 5),
                OrderItem("margherita", "Small", 4),
                OrderItem("hawaii", "Large", 1),
                OrderItem("margherita", "Medium", 2),
                OrderItem("capricciosa", "Small", 7),
            ],
            900,
        ),
        # 5개가 100보다 저렴해서 D2 손해 → D1 적용 (5개 ≥ 3, cheapest=10 무료)
        (
            [Pizza("cheap", 10, 12, 15)],
            [OrderItem("cheap", "Small", 5)],
            # base=50, D2: savings=50-100=-50 미적용, D1: -10 → 40
            40,
        ),
        # 같은 이름 여러 사이즈 혼합, 가장 비싼 5개 선택 검증
        (
            [Pizza("mix", 10, 30, 50)],
            [
                OrderItem("mix", "Small", 3),  # 10×3=30
                OrderItem("mix", "Medium", 2),  # 30×2=60
                OrderItem("mix", "Large", 2),  # 50×2=100
            ],
            # base=190, top5=[50,50,30,30,10]=170 → savings=70 → 120
            120,
        ),
    ],
)
def test_discount2_buy5_for_100(menu, order, expected):
    assert solution(menu, order) == expected


# ── Discount 3: Large → free Small (same name) ──────────────────────────────


@pytest.mark.parametrize(
    "menu, order, expected",
    [
        # 기본 예제: margherita 1Large+1Small(무료), capricciosa 2Large+2Small(무료)
        (
            [
                Pizza("margherita", 7, 8, 10),
                Pizza("hawaii", 8, 9, 12),
                Pizza("capricciosa", 5, 7, 13),
            ],
            [
                OrderItem("margherita", "Small", 3),
                OrderItem("capricciosa", "Large", 2),
                OrderItem("hawaii", "Large", 3),
                OrderItem("margherita", "Large", 1),
                OrderItem("hawaii", "Medium", 1),
                OrderItem("capricciosa", "Small", 5),
                OrderItem("capricciosa", "Medium", 1),
            ],
            117,
        ),
        # Small이 Large보다 많을 때: free = Large 수만큼
        (
            [Pizza("z", 10, 15, 20)],
            [
                OrderItem("z", "Large", 2),
                OrderItem("z", "Small", 5),
            ],
            # base=40+50=90, savings=2×10=20 → 70
            70,
        ),
        # Large가 Small보다 많을 때: free = Small 수만큼
        (
            [Pizza("z", 10, 15, 20)],
            [
                OrderItem("z", "Large", 5),
                OrderItem("z", "Small", 2),
            ],
            # base=100+20=120, savings=2×10=20 → 100
            100,
        ),
        # Small이 없을 때: D3 미적용, D1 적용 (3개 ≥ 3, cheapest=20 무료)
        (
            [Pizza("z", 10, 15, 20)],
            [OrderItem("z", "Large", 3)],
            # base=60, D3 savings=0, D1: -20 → 40
            40,
        ),
    ],
)
def test_discount3_large_free_small(menu, order, expected):
    assert solution(menu, order) == expected


# ── Discount 4: Buy 3 Large, pay for 3 Medium ───────────────────────────────


@pytest.mark.parametrize(
    "menu, order, expected",
    [
        # 기본 예제: newyorker(130-9=121), boston×2(10-5=5) top3=131 → 233-131=102
        # (
        #     [
        #         Pizza("boston", 7, 5, 10),
        #         Pizza("hawaii", 8, 9, 12),
        #         Pizza("newyorker", 8, 9, 130),
        #         Pizza("philadelphia", 5, 10, 13),
        #     ],
        #     [
        #         OrderItem("boston", "Small", 3),
        #         OrderItem("hawaii", "Large", 3),
        #         OrderItem("newyorker", "Large", 1),
        #         OrderItem("boston", "Large", 2),
        #         OrderItem("philadelphia", "Large", 2),
        #     ],
        #     102,
        # ),
        # Large 정확히 3개
        (
            [Pizza("a", 5, 8, 20), Pizza("b", 5, 6, 15)],
            [
                OrderItem("a", "Large", 2),
                OrderItem("b", "Large", 1),
            ],
            # base=40+15=55, savings=(20-8)×2+(15-6)×1=24+9=33
            # top3=[12,12,9]=33 → 55-33=22
            22,
        ),
        # Large가 3개 미만: 할인 불가
        (
            [Pizza("a", 5, 8, 20)],
            [OrderItem("a", "Large", 2)],
            # base=40, discount4 불가
            40,
        ),
        # price_L < price_M: D4 적용하면 손해 → D1 적용 (3개≥3, cheapest=10 무료)
        # (
        #     [Pizza("weird", 5, 20, 10)],
        #     [OrderItem("weird", "Large", 3)],
        #     # base=30, D4: top3_savings=-30 → cost=60 (손해), D1: -10 → 20
        #     20,
        # ),
    ],
)
def test_discount4_buy3large_pay_medium(menu, order, expected):
    assert solution(menu, order) == expected


# ── Corner case: No discount applicable ─────────────────────────────────────


@pytest.mark.parametrize(
    "menu, order, expected",
    [
        # 피자 2개: 모든 할인 조건 미충족
        (
            [
                Pizza("margherita", 7, 8, 10),
                Pizza("hawaii", 8, 9, 12),
                Pizza("capricciosa", 5, 7, 13),
            ],
            [
                OrderItem("margherita", "Small", 1),
                OrderItem("hawaii", "Large", 1),
            ],
            19,
        ),
        # 피자 1개
        (
            [Pizza("solo", 100, 200, 300)],
            [OrderItem("solo", "Large", 1)],
            300,
        ),
    ],
)
def test_no_discount_applicable(menu, order, expected):
    assert solution(menu, order) == expected


# ── 최적 할인 선택: 여러 할인 중 가장 이득인 것 선택 ──────────────────────────


def test_chooses_best_discount():
    """D1(cheapest free)보다 D4(3Large→Medium)가 더 이득인 경우."""
    menu = [Pizza("bigdiff", 1, 1, 1000)]
    order = [OrderItem("bigdiff", "Large", 3)]
    # base=3000
    # D1: -1000 → 2000
    # D4: savings=(1000-1)×3=2997 → 3000-2997=3
    assert solution(menu, order) == 3
