"""
给定一个没有重复数字的序列，返回其所有可能的全排列。
示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #DPS with swapping
        res = []
        if len(nums) == 0:
        	return res
        self.get_permute(res, nums, 0)
        return res

    def get_permute(self, res, nums, index):
    	if index == len(nums):
    		res.append(list(nums))
    		return
    	for i in range(index, len(nums)):
    		nums[i], nums[index] = nums[index], nums[i]
    		# s(n) = 1 + s(n-1)
    		self.get_permute(res, nums, index + 1)
    		nums[i], nums[index] = nums[index], nums[i]
    		