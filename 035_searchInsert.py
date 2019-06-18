"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
        	mid = (l + r) / 2
        	if nums[mid] < target:
        		l = mid + 1
        	else:
        		r = mid
        if nums[l] < target:
        	return l + 1
        return l 