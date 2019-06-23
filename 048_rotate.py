"""
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #rotate from outside to inside
        if matrix is None or len(matrix) == 1:
            return
        ls = len(matrix)
        for i in range(ls / 2):
            # border
            begin, end = i, ls - 1 - i
            for k in range(ls - 2 * i - 1):
                temp = matrix[end - k][begin]
                matrix[end - k][begin] = matrix[end][end - k]
                matrix[end][end - k] = matrix[begin + k][end]
                matrix[begin + k][end] = matrix[begin][begin + k]
                matrix[begin][begin + k] = temp
        return