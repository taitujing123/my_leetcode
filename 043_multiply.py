"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        res = ''
        ls1, ls2, = len(num1), len(num2)
        ls = ls1 + ls2
        #list stores int
        arr = [0] * ls
        for i in reversed(range(ls1)):
        	for j in reversed(range(ls2)):
        		# store the direct results of multiply two ints
        		arr[i + j + 1] += int(num1[i]) * int(num2[j])
        for i in reversed(range(1, ls)):
        	#digital plus
        	arr[i - 1] += arr[i] / 10
        	arr[i] %= 10
        pos = 0
        #to string
        if arr[pos] == 0:
        	pos += 1
        while pos < ls:
        	res = res + str(arr[pos])
        	pos += 1
        return res
