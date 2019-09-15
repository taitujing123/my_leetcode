"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]

        #第一维表示天数，第二维表示完成几笔交易，第三纬度表示是否持有股票

        profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        profit[0][1][0], profit[0][1][1] = float('-inf'), float('-inf')
        profit[0][2][0], profit[0][2][1] = float('-inf'), float('-inf')

        for i in range(1, len(prices)):
            profit[i][0][0] = profit[i-1][0][0]
            profit[i][0][1] = max(profit[i-1][0][1], profit[i-1][0][0] - prices[i])

            profit[i][1][0] = max(profit[i-1][1][0], profit[i-1][0][1] + prices[i])
            profit[i][1][1] = max(profit[i-1][1][1], profit[i-1][1][0] - prices[i])

            profit[i][2][0] = max(profit[i-1][2][0], profit[i-1][1][1] + prices[i])

        end = len(prices) - 1
        return max(profit[end][0][0], profit[end][1][0], profit[end][2][0])



