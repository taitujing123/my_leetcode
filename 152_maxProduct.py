"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        max_here = min_here = max_so_far = nums[0]
        for i in range(1, len(nums)):
            mx, mn = max_here, min_here
            max_here = max(max(mx * nums[i], nums[i]), mn * nums[i])
            min_here = min(min(mx * nums[i], nums[i]), mn * nums[i])
            max_so_far = max(max_here, max_so_far)
        return max_so_far