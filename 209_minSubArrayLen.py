"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
        	return 0
        if s == 0:
        	return 0
        if s == len(nums):
        	return len(nums)
        left = right = 0
        subSum = 0
        length = len(nums)
        for right, item in enumerate(nums):
        	subSum += item
        	while subSum >= s:
        		length = min(length, right - left + 1)
        		subSum -= item
        		while sub_sum >= s:
                length = min(length, right - left + 1)
                sub_sum -= nums[left]
                left += 1
        return length










