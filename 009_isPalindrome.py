"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False
        ls = 0
        tmp = x
        while tmp != 0:
        	tmp = tmp // 10
        	ls += 1
        tmp = x
        for i in range(ls/2):
        	right = tmp % 10
        	left = tmp / (10**(ls-2*i-1))
        	left = left % 10
        	if left != right:
        		return False
        	tmp = tmp // 10
        return True
