"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sort_nums = nums
        sort_nums.sort()
        ls = len(nums)
        res = {}
        pairs = {}
        for i in range(ls-3):
        	for j in range(i+1, ls-2):
        		res_2 = sort_nums[i] + sort_nums[j]
        		try:
        			pairs[target - res_2].append([i,j])
        		except Keyerror:
        			pairs[target - res_2] = [[i,j]]
        for key, temp in pairs.item():
        	for pair in temp:
        		j = pair[1] + 1
        		k = ls - 1
        		while j < k:
        			current = sort_nums[j] + sort_nums[k]
        			if current == key:
        				result = (sort_nums[pair[0]],sort_nums[pair[1]],sort_nums[j],sort_nums[k])
        				res[result] = True
        				j += 1
        			elif current < key:
        				j += 1
        			else:
        				k -= 1
        return res.keys()









