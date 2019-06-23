"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return []
        i, j, di, dj = 0, 0, 0, 1
        m, n = len(matrix), len(matrix[0])
        for v in xrange(m * n):
            res.append(matrix[i][j])
            matrix[i][j] = ''
            if matrix[(i + di) % m][(j + dj) % n] == '':
                # (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
                # then loop
                di, dj = dj, -di
            i += di
            j += dj
        return res