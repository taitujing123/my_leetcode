"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 0:
            return 0
        dmap = [[0] * (n + 1) for _ in range(m + 1)]
        dmap[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in  range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dmap[i][j] = 0
                else:
                    dmap[i][j] = dmap[i][j + 1] + dmap[i + 1][j]
        return dmap[0][0]