def stonks_gud(A):
    min_, max_profit = float('inf'), 0.0
    for price in A:
        max_profit_for_today = price - min_
        max_profit = max(max_profit, max_profit_for_today)
        min_ = min(min_, price)
    print('For stonk', A, 'the most profit is', max_profit)
    return max_profit


if __name__ == "__main__":
    prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    stonks_gud(prices)
