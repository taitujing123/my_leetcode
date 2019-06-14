class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        max_int, min_int = pow(2,31) - 1, -pow(2,31)
        result, pos = 0, 0
        ls = len(str)
        while pos < ls and str[pos] == ' ':
        	pos += 1
        if pos < ls and str[pos] == '-':
        	sign = -1
        	pos += 1
        elif pos < ls and str[pos] == '+':
        	pos += 1
        while  pos < ls and ord(str[pos]) >= ord('0') and ord(str[pos]) <= ord('9'):
        	num = ord(str[pos]) - ord('0')
        	if result > max_int / 10 or (result == max_int / 10 and num >= 8):
        		if sign == -1:
        			return min_int
        		return max_int
        	result = result * 10 + num
        	pos += 1
        return sign * result