"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = nums.sort()
        ls = len(nums)
        for i in range(ls-2):
        	if i > 0 and nums[i] == nums[i-1]:
        		continue
        	j = i + 1
        	k = ls - 1
        	while j < k:
        		curr = nums[i] + nums[j] + nums[k]
        		if curr == 0:
        			res.append([nums[i],nums[j],nums[k]])
        			while j < k and nums[j] == nums[j+1]:
        				j += 1
        			while j < k and num[k] == num[k-1]:
        				k -= 1
        			j += 1
        			k -= 1
        		elif curr < 0:
        			j += 1
        		else:
        			k -= 1
        return res
