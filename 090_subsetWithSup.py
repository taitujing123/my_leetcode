"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        begin = 0
        for index in range(len(nums)):
            if index == 0 or nums[index] != nums[index - 1]:
                # generate all
                begin = 0
            size = len(res)
            # use existing subsets to generate new subsets
            for j in range(begin, size):
                curr = list(res[j])
                curr.append(nums[index])
                res.append(curr)
            # avoid duplicate subsets
            begin = size
        return res
