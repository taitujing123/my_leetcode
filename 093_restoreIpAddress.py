"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ls = len(s)
        if ls == 0 or ls > 12:
            return []
        res = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    m = ls - i - j - k
                    if m > 0 and m <= 3:
                        add1 = s[0:i]
                        add2 = s[i:i + j]
                        add3 = s[i + j:i + j + k]
                        add4 = s[i + j + k:]
                        if self.isValid(add1) and self.isValid(add2) and \
                                        self.isValid(add3) and self.isValid(add4):
                            res.append(add1 + '.' + add2 + '.' + add3 + '.' + add4)
        return res

    def isValid(self, add):
        if len(add) == 1:
            return True
        if add[0] == '0':
            return False
        if int(add) <= 255:
            return True
        return False