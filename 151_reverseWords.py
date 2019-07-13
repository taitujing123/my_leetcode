"""
给定一个字符串，逐个翻转字符串中的每个单词。

 

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip(' ')
        array_s = []
        last = ' '
        # remove multiple spaces
        for i in range(len(s)):
            if s[i] != ' ':
                array_s.append(s[i])
            else:
                if last != ' ':
                    array_s.append(s[i])
            last = s[i]
        array_s = array_s[::-1]
        ls, pos = len(array_s), 0
        for i in range(ls + 1):
            if i == ls or array_s[i] == ' ':
                self.reverse(array_s, pos, i)
                pos = i + 1
        return ''.join(array_s)

    def reverse(self, array_s, begin, end):
        for i in range((end - begin) / 2):
            array_s[begin + i], array_s[end - i - 1] = array_s[end - i - 1], array_s[begin + i]

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip(' ')
        array_s = []
        last = ' '
        # remove multiple spaces
        for i in range(len(s)):
            if s[i] != ' ':
                array_s.append(s[i])
            else:
                if last != ' ':
                    array_s.append(s[i])
            last = s[i]
        new_str = ''.join(array_s)
        new_array = new_str.split(' ')
        res = []
        for cha in new_array:
            if cha != ' ':
                res.append(cha)
        
        res = res[::-1]
        output = []
        for i in range(len(res)):
            if i == len(res) - 1:
                output.append(res[i])
            else:
                output.append(res[i] + ' ')
        
        return ''.join(output)

