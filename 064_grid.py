"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        pathmap = []
        for i in range(height):
            pathmap.append([100000000000] * width)
        pathmap[0][0] = grid[0][0]
        for i in range(height):
            for j in range(width):
                compare = [pathmap[i][j]]
                if i - 1 >= 0:
                    compare.append(pathmap[i - 1][j] + grid[i][j])
                if j - 1 >= 0:
                    compare.append(pathmap[i][j - 1] + grid[i][j])
                # min choice
                pathmap[i][j] = min(compare)
        return pathmap[-1][-1]