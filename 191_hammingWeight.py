"""
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

 

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-1-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://leetcode.com/articles/number-1-bits/
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count