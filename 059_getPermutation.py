"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        pos = [0, 0]
        move = (0, 1)
        for index in range(1, n * n + 1):
        	res[pos[0]][pos[1]] = index
        	if res[(pos[0] + move[0]) % n][(pos[1] + move[1]) % n] > 0:
        		# (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
        		move = (move[1], -1 * move[0])
        	pos[0] = pos[0] + move[0]
        	pos[1] = pos[1] + move[1]
        return res