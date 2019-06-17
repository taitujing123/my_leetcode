"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
        	return ['()']
        last_list = self.generateParenthesis(n-1)
        res = []
        for t in last_list:
        	curr = t + ')'
        	for index in range(len(curr)):
        		if curr[index] == ')':
        			res.append(curr[:index] + '(' + curr[index:])
        return list(set(res))