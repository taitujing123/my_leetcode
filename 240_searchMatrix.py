"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and i <= m - 1 and j >= 0 and j <= n - 1:
            if target == matrix[i][j]:
                return True
            while j >= 0 and j <= n - 1 and i >= 0 and i <= m - 1 and target > matrix[i][j]:
                j += 1
            while j >= 0 and j <= n - 1 and i >= 0 and i <= m - 1 and target < matrix[i][j]:
                i -= 1
        return False
                
                