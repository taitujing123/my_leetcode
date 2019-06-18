"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ls = len(nums)
        if ls <= 1:
            return nums
        pair = []
        for i in range(ls):
            for j in range(i + 1, ls):
                # append ascending order pair
                if nums[i] < nums[j]:
                    pair.append([i,j])
        pos = 0
        if len(pair) > 0:
            self.swap(nums, pair[-1][0], pair[-1][1])
            pos = pair[-1][0] + 1
        # sort from pos
        for i in range(pos, ls):
            for j in range(i + 1, ls):
                if nums[i] > nums[j]:
                    self.swap(nums, i, j)

    def swap(self, nums, index1, index2):
        if index1 == index2:
            return nums[index1], nums[index2] = nums[index2], nums[index1]

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = -1
        ls = len(nums)
        for i in range(ls - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pos = i - 1
                break
        if pos == -1:
            self.re_order(nums, 0, ls - 1)
            return
        for i in range(ls - 1, -1, -1):
            if nums[pos] < nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
                self.re_order(nums, pos + 1, ls - 1)
                break
    
    def re_order(self, a, start, end):
        for i in range(0, (end - start + 1) // 2):
            a[start + i], a[end - i] = a[end - i], a[start + i]

