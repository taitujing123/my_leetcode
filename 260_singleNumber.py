"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pivot = 0
        for i in nums:
            pivot ^= i
        pivot = pivot & (-pivot)

        a, b = 0, 0
        for i in nums:
            if i & pivot == pivot:
                a ^= i
            else:
                b ^= i

        return [a, b]

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1,2,1,3,2,5]))