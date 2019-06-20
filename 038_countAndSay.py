"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-and-say
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
        	return '1'
        x = '1'
        while n > 1:
        	#each round, read itself
        	x = self.count(x)
        	n -= 1
        return x

    def count(self, x):
    	m = list(x)
    	res = []
    	m.append(None)
    	i, j = 0, 0
    	while i < len(m) - 1:
    		j += 1
    		if m[j] != m[i]:
    			#note j - i is the count of m[i]
    			res += [j - i, m[i]]
    			i = j
    	return ''.join(str(s) for s in res)




