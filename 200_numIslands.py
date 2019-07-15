"""
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #BFS with marks
        if grid is None or len(grid) == 0:
        	return 0
        islands = 0
        for i in range(len(grid)):
        	for j in range(len(gird[0])):
        		if grid[i][j] == '1':
        			self.explore(grid, i, j)
        			islands += 1
        return islands

    def explore(self, grid, i, j):
    	grid[i][j] = 'X'
    	if i - 1 >= 0 and grid[i - 1][j] == '1':
    		self.explore(grid, i - 1, j)
    	if j - 1 >= 0 and grid[i][j - 1] == '1':
    		self.explore(grid, i, j - 1)
    	if i + 1 < len(grid) and grid[i + 1][j] == '1':
    		self.explore(grid, i + 1, j)
    	if j + 1 < len(grid[i]) and grid[i][j + 1] == '1':
    		self.explore(grid, i, j + 1)