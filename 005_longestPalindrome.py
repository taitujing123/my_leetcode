"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # my solution
        # expand string according to Manacher algorithm
        # but extend radius step by step
        ls = len(s)
        if ls <= 1 or len(set(s)) == 1:
        	return s
        #create a new list like this:"abc"->"a#b#c"
        temp_s = '#'.join('{}'.format(s))
        tls = len(temp_s)
        seed = range(1, tls - 1)
        #this table stores the max length palindrome
        len_table = [0] * tls
        for step in range(1, tls / 2 + 1):
        	final = []
        	for pos in seed:
        		if pos - step < 0 or pos + step >= tls:
        			continue
        		if temp_s[pos - step] != temp_s[pos + step]:
        			continue
        		final.append(pos)
        		if temp_s[pos - step] == '#':
        			continue
        		len_table[pos] = step
        	seed = final
        max_pos, max_step = 0, 0
        for i, s in enumerate(len_table):
        	if s >= max_step:
        		max_step = s
        		max_pos = i
        return temp_s[max_pos - max_step:max_pos + max_step + 1].translate(None,'#')
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
            # 调试语句
            # for item in dp:
            #     print(item)
            # print('---')
        return res

