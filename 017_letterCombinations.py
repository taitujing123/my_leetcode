"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dmap = {'2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' ',
        None: None}

        result = []
        ls = len(digits)
        if ls == 0:
        	return result
        current = digits[0]
        posfix = self.letterCombinations(digits[1:])
        for t in dmap[current]:
        	if len(posfix) > 0:
        		for p in posfix:
        			temp = t + p
        			result.append(temp)
        	else:
        		result.append(t)

        return result
