import pytest
from src.leetcode.best_time_to_buy_and_sell_stock_121 import max_profit


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
        ([3, 2, 6, 5, 0, 3], 4),
    ],
)
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected
