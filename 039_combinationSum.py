"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [[ ] for _ in range(target + 1)]
        dp[0].append([])
        for i in range(1, target + 1):
        	for j in range(len(candidates)):
        		if candidates[j] > i:
        			break
        		for k in range(len(dp[i - candidates[j]])):
        			temp = dp[i - candidates[j]][k][:]
        			if len(temp) > 0 and temp[-1] > candidates[j]:
        				continue
        			temp.append(candidates[j])
        			dp[i].append(temp)
        return dp[target]