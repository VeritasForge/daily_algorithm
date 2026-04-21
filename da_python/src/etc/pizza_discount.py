"""
Pizza Party Discount
(Codility-style problem)

문제 원문:
    You are ordering pizzas for a party. You are given an order (a list of items
    to buy) and a menu (a list of all available items and their prices).

    The pizza shop offers the following discounts:
        Discount 1: "Buy 3, the cheapest one is free!"
        Discount 2: "Buy 5 for 100!"
        Discount 3: "For every Large pizza, get a free Small one!"
        Discount 4: "Buy 3 Large, pay for 3 Medium!"

    Your goal is to minimize the total cost of the order by using at most one
    of the discounts offered by the pizza shop.

    Discount 1: Buy 3, the cheapest one is free!
        When your order contains at least three pizzas (not necessarily different),
        you can choose not to pay for the cheapest pizza in the entire order.

    Discount 2: Buy 5 for 100!
        When your order contains at least five pizzas with the same name, you can
        choose five of them to cost 100 in total. This discount can be used at
        most once per order and you cannot split your order.

    Discount 3: For every Large pizza, get a free Small one!
        When your order contains a "Large" and a "Small" pizza with the same name,
        you can get the "Small" one for free. You can use this discount as many
        times as you want, provided the conditions are met and you are not using
        any other discount.

    Discount 4: Buy 3 Large, pay for 3 Medium!
        When your order contains at least three "Large" pizzas, you can choose
        exactly three and pay for them as if they were "Medium" pizzas with the
        same names. You can use this discount at most once per order.

    Return the minimum amount to be paid when using at most one of the discounts
    offered by the pizza shop (or no discount if none apply or none help).

문제 설명:
    파티를 위해 피자를 주문할 때 4가지 할인 중 최대 하나를 선택해
    총 주문 비용을 최소화한다.

    할인 1: Buy 3, the cheapest one is free!
        - 주문 피자 총 수 ≥ 3이면, 전체 주문에서 가장 싼 피자 1개 무료.

    할인 2: Buy 5 for 100!
        - 같은 이름의 피자가 5개 이상이면, 그 중 5개를 합계 100으로 구매.
        - 주문당 최대 1회 사용. 가장 절약이 큰 이름/조합을 선택.

    할인 3: For every Large pizza, get a free Small one! (같은 이름)
        - Large 1개당 같은 이름 Small 1개 무료.
        - 이 할인 내에서 여러 번 적용 가능.

    할인 4: Buy 3 Large, pay for 3 Medium!
        - Large 피자가 3개 이상이면 정확히 3개를 골라 Medium 가격으로 지불.
        - 주문당 최대 1회 사용. 절약이 최대인 3개 선택.

입력:
    menu: list[Pizza]      - 피자 이름과 S/M/L 가격 목록
    order: list[OrderItem] - 구매할 피자 이름, 사이즈, 수량 목록

출력:
    int - 4가지 할인 중 최대 하나를 적용했을 때의 최소 총 비용

제약 조건:
    - N (menu 길이): 1 ≤ N ≤ 10
    - M (order 길이): 1 ≤ M ≤ 30
    - quantity: 1 ≤ quantity ≤ 10
    - price: 1 ≤ price ≤ 1,000
    - size: "Small" | "Medium" | "Large" (case-insensitive)
    - order의 모든 이름은 menu에 존재
    - (name, size) 조합은 order에서 유일
"""

from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Pizza:
    name: str
    price_S: int
    price_M: int
    price_L: int


@dataclass
class OrderItem:
    name: str
    size: str
    quantity: int


def solution(menu: list[Pizza], order: list[OrderItem]) -> int:
    menu_map = {pizza.name: pizza for pizza in menu}
    discounted_prices = []

    def get_price(name: str, size: str) -> int:
        size = size.lower()
        pizza = menu_map[name]

        if size == "small":
            return pizza.price_S
        elif size == "medium":
            return pizza.price_M
        return pizza.price_L

    total_prices = sum(get_price(o.name, o.size) * o.quantity for o in order)

    # Discount 1: Buy 3, the cheapest one is free!
    if sum(o.quantity for o in order) >= 3:
        o = min(order, key=lambda o: get_price(o.name, o.size))
        discounted_prices.append(get_price(o.name, o.size))

    # Discount 2: Buy 5 for 100!
    ordered_menu_map = defaultdict(list[int])
    for o in order:
        ordered_menu_map[o.name].extend([get_price(o.name, o.size)] * o.quantity)

    max_price = 0
    for menu, prices in ordered_menu_map.items():
        if len(prices) < 5:
            continue

        total_price = sum(sorted(prices, reverse=True)[:5])
        if max_price < total_price:
            max_price = total_price

    if max_price > 0:
        discounted_prices.append(max_price - 100)

    # Discount 3:  For every Large pizza, get a free Small one!
    ordered_menu_prices = defaultdict(lambda: defaultdict(tuple[int, int]))
    total_discounted_price = 0
    for o in order:
        if o.size.lower() == "medium":
            continue

        ordered_menu_prices[o.name][o.size.lower()] = (
            get_price(o.name, o.size),
            o.quantity,
        )

    for name, size_price_count in ordered_menu_prices.items():
        if len(size_price_count) != 2:
            continue

        _, large_count = size_price_count["large"]
        small_price, small_count = size_price_count["small"]

        total_discounted_price += small_price * (
            small_count if large_count >= small_count else large_count
        )

    discounted_prices.append(total_discounted_price)

    # Discount 4: Buy 3 large, pay for 3 Medium!
    ordered_large_menu = defaultdict(tuple[int, int])
    max_discounted_price = 0
    for o in order:
        if o.size.lower() != "large":
            continue

        ordered_large_menu[o.name] = (get_price(o.name, o.size), o.quantity)

    for name, (price, quantity) in ordered_large_menu.items():
        if quantity < 3:
            continue

        discounted_price = (price * quantity) - (
            menu_map[name].price_M * 3 if quantity > 3 else quantity
        )
        if max_discounted_price < discounted_price:
            max_discounted_price = discounted_price

    discounted_prices.append(max_discounted_price)

    # result
    max_discounted_price = max(discounted_prices)
    return (
        total_prices - max_discounted_price
        if max_discounted_price > 0
        else total_prices
    )


# def solution(menu: list[Pizza], order: list[OrderItem]) -> int:
#     # 메뉴 이름 → Pizza 객체 맵
#     menu_map: dict[str, Pizza] = {pizza.name: pizza for pizza in menu}
#
#     def get_price(name: str, size: str) -> int:
#         pizza = menu_map[name]
#         s = size.lower()
#         if s == "small":
#             return pizza.price_S
#         if s == "medium":
#             return pizza.price_M
#         return pizza.price_L  # large
#
#     # 전체 피자를 개별 가격 리스트로 펼치기
#     all_prices: list[int] = []
#     for item in order:
#         price = get_price(item.name, item.size)
#         all_prices.extend([price] * item.quantity)
#
#     base_cost = sum(all_prices)
#     costs: list[int] = [base_cost]  # 할인 없음
#
#     # ── Discount 1: Buy 3, cheapest one is free ─────────────────────────────
#     if len(all_prices) >= 3:
#         costs.append(base_cost - min(all_prices))
#
#     # ── Discount 2: Buy 5 of same name for 100 ──────────────────────────────
#     name_prices: dict[str, list[int]] = defaultdict(list)
#     for item in order:
#         price = get_price(item.name, item.size)
#         name_prices[item.name].extend([price] * item.quantity)
#
#     best_d2_savings = 0
#     for prices in name_prices.values():
#         if len(prices) >= 5:
#             # 절약 최대화: 가장 비싼 5개 선택 → (정상가 합 - 100)
#             top5_sum = sum(sorted(prices, reverse=True)[:5])
#             savings = top5_sum - 100
#             best_d2_savings = max(best_d2_savings, savings)
#
#     if best_d2_savings > 0:
#         costs.append(base_cost - best_d2_savings)
#
#     # ── Discount 3: Large 1개당 같은 이름 Small 1개 무료 ────────────────────
#     savings_d3 = 0
#     for name, pizza in menu_map.items():
#         large_qty = small_qty = 0
#         for item in order:
#             if item.name == name:
#                 if item.size.lower() == "large":
#                     large_qty += item.quantity
#                 elif item.size.lower() == "small":
#                     small_qty += item.quantity
#         free_count = min(large_qty, small_qty)
#         savings_d3 += free_count * pizza.price_S
#
#     if savings_d3 > 0:
#         costs.append(base_cost - savings_d3)
#
#     # ── Discount 4: Buy 3 Large, pay for 3 Medium ───────────────────────────
#     large_savings: list[int] = []
#     for item in order:
#         if item.size.lower() == "large":
#             pizza = menu_map[item.name]
#             # 절약액 = price_L - price_M (음수면 손해)
#             large_savings.extend([pizza.price_L - pizza.price_M] * item.quantity)
#
#     if len(large_savings) >= 3:
#         # 절약 최대화: savings가 큰 순으로 3개 선택
#         top3_savings = sum(sorted(large_savings, reverse=True)[:3])
#         costs.append(base_cost - top3_savings)
#
#     return min(costs)
