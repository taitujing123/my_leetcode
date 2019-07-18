"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #dp[j] = min(dp[j], dp[j-1], prev) + 1
        #O(n) space
        if matrix is None or len(matrix) == 0:
        	return 0
        rows, cols, res, prev = len(matrix), len(matrix[0]), 0, 0
        dp = [0] * (cols + 1)
        for i in range(1, row + 1):
        	for j in range(1, cols + 1):
        		temp = dp[j]
        		if matrix[i - 1][j - 1] == '1':
        			dp[j] = min(dp[j], dp[j - 1], prev) + 1
        			res = max(res, dp[j])
        		else:
        			dp[j] = 0
        		prev = temp
        return res * res