def maxProfit(prices : List[int]) -> int:
    if prices == []:
        return 0
    max_profit = 0
    min_num = prices[0]
    for i in range(len(prices)):
        if min_num > prices[i]:
            min_num = prices[i]
        profit = prices[i] - min_num
        if profit > max_profit:
            max_profit = profit
    return max_profit

    