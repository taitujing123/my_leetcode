class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
        	return s
        # calculate period
        p = 2 * (numRows - 1)
        result = [""] * numRows
        for i in range(len(s)):
        	floor = i % p
        	if floor >= p // 2:
        		floor = p - floor
        	result[floor] += s[i]
        return "".join(result)

