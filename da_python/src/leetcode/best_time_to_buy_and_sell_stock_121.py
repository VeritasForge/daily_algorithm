from sys import maxsize

"""
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

121. Best Time to Buy and Sell Stock

You are given an array of prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def max_profit(prices: list[int]) -> int:
    """
    Calculates the maximum profit that can be achieved.

    Args:
        prices: A list of integers representing the stock prices.

    Returns:
        The maximum profit.
    """
    min_price = maxsize
    max_profit = 0

    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(price - min_price, max_profit)

    return max_profit
