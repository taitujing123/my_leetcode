"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
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
        res = 0
        profit = [[0 for i in range(3)] for i in range(len(prices))]

        # 第二维的0，1，2分别表示无购买股票，购入股票，已经卖出股票
        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0
        for i in range(1, len(prices)):
            profit[i][0] = profit[i - 1][0]
            profit[i][1] = max(profit[i - 1][1], profit[i - 1][0] - prices[i])
            profit[i][2] = profit[i - 1][1] + prices[i]
            res = max(res, profit[i][0], profit[i][1], profit[i][2])

        return res
