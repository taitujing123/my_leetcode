"""
给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。

示例 1:

输入: 12
输出: 21
示例 2:

输入: 21
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [int(x) for x in str(n)]
        if sorted(nums)[::-1] == nums:
            return -1
        m = len(nums)
        for i in range(m - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(m - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i + 1:] = sorted(nums[i + 1:])
                        break
                break
        res = 0
        for i in nums:
            res = 10 * res + i
        return res if res<2**31 else -1
