class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: :List[int]
		"""
		# two point
		nums_sort = [(value, index) for index, value in enumerate(nums)]
		nums_sort.sort()
		begin, end = 0, len(nums)-1
		while begin < end:
			if target == nums_sort[begin][0] + nums_sort[end][0]:
				return [[nums_sort[begin][1],nums_sort[end][1]]
			elif target > nums_sort[begin][0] + nums_sort[end][0]:
				begin += 1
			else:
				end -= 1

		return None