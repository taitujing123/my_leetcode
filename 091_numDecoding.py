"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = len(s)
        if ls == 0:
            return 0
        dp = [0] * ls
        for index in range(ls):
            if index >= 1 and int(s[index - 1:index + 1]) < 27 and int(s[index - 1:index + 1]) >= 10:
                if index == 1:
                    dp[index] = 1
                else:
                    # 11-26
                    dp[index] += dp[index - 2]
            if int(s[index]) != 0:
                if index == 0:
                    dp[index] = 1
                else:
                    # 1-9
                    dp[index] += dp[index - 1]
        return dp[ls - 1]
