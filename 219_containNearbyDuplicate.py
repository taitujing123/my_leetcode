"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        check = {}
        for i in range(len(nums)):
            try:
                check[nums[i]].append(i)
            except:
                check[nums[i]] = [i]
        # hash all value with its index
        # then check the difference between indexes under the same value
        for _, v in check.items():
            if len(v) >= 2:
                pos = 0
                while pos + 1 < len(v):
                    if v[pos + 1] - v[pos] <= k:
                        return True
                    pos += 1
        return False