"""
给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

示例 1:

输入: [1, 5, 2]
输出: False
解释: 一开始，玩家1可以从1和2中进行选择。
如果他选择2（或者1），那么玩家2可以从1（或者2）和5中进行选择。如果玩家2选择了5，那么玩家1则只剩下1（或者2）可选。
所以，玩家1的最终分数为 1 + 2 = 3，而玩家2为 5。
因此，玩家1永远不会成为赢家，返回 False。
示例 2:

输入: [1, 5, 233, 7]
输出: True
解释: 玩家1一开始选择1。然后玩家2必须从5和7中进行选择。无论玩家2选择了哪个，玩家1都可以选择233。
最终，玩家1（234分）比玩家2（12分）获得更多的分数，所以返回 True，表示玩家1可以成为赢家。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/predict-the-winner
著作权归领扣网络所有。商业转载请联系官方授权，if 非商业转载请注明出处.
"""
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) % 2 == 0:
            return True
        dp = {}
        def max_get(i, j):
            if j - i < 3:
                _max = max(nums[i:j])
                dp[i, j] = _max, sum(nums[i:j]) - _max
            else:
                x1, y1 = max_get(i+1, j)
                x2, y2 = max_get(i, j-1)
                if nums[i] + y1 > nums[j] + y2:
                    dp[i, j] = nums[i] + y1, x1
                else:
                    dp[i, j] = nums[j] + y2, x2

            return dp[i, j]
        x, y = max_get(0, len(nums))
        return x >= y
