"""
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
 

注意:

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 1:
        	return True
        sum_num = sum(nums)
        if sum_num % k != 0:
        	return False
        avg = sum_num // k
        n = len(nums)
        if n < k:
        	return False
        visited = set()

        def dfs(k, tmp_sum, loc):
        	if tmp_sum == avg:
        		return dfs(k-1,0,0)
        	if k == 1:
        		return True
        	for i in range(loc, n):
        		if i not in visited and nums[i] + tmp_sum <= avg:
        			visited.add(i)
        			if dfs(k, tmp_sum+nums[i], i+1):
        				return True
        			visited.remove(i)
        	return False
        return dfs(k,0,0)