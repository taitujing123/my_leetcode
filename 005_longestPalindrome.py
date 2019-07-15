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
