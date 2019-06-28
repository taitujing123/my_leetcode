"""
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        lsa, lsb = len(a), len(b)
        pos, plus, curr = -1, 0, 0
        # plus a[pos], b[pos] and curr % 2
        while (lsa + pos) >= 0 or (lsb + pos) >= 0:
            if (lsa + pos) >= 0:
                curr += int(a[pos])
            if (lsb + pos) >= 0:
                curr += int(b[pos])
            res = str(curr % 2) + res
            curr /= 2
            pos -= 1
        if curr == 1:
            res = '1' + res
        return res