"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return [-1, -1]
        min = 0
        max = length - 1
        while min <= max:
        	pos = (min + max) / 2
        	if nums[pos] > target:
        		max = pos - 1
        	elif nums[pos] < target:
        		min = pos + 1
        	else:
        		#when nums[pos] == target
        		#find the min and max
        		for i in range(min, max + 1):
        			if nums[i] == target:
        				if min < i and nums[min] != nums[i]:
        					min = i
        				max = i
        		return [min, max]
        return [-1, -1]