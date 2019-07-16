"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # bottom-up dp
        if amount == 0:
            return 0
        if coins is None or len(coins) == 0:
            return -1
        coins.sort()
        dp = [1000000000] * (amount + 1)
        for i in range(1, amount + 1):
        	for coin in coins:
        		if i == coin:
        			dp[i] = 1
        			break
        		elif i > coin:
        			dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == 1000000000:
        	return -1
        return dp[amount]
