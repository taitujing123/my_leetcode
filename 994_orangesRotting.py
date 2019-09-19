"""在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotting-oranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
采用栈来压入所有腐烂的橘子，每次弹出一个腐烂的橘子来传染周围的橘子直到栈空
最终需要判断是否还有新鲜橘子则返回-1，否则返回时间
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x, y, time = len(grid), len(grid[0]), 0
        locs, stack = [[-1,0],[1,0],[0,-1],[0,1]], []
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 2:
                    stack.append((i, j, 0))
        while stack:
            i, j, time = stack.pop(0)
            for loc in locs:
                loc_x, loc_y = i + loc[0], j + loc[1]
                if 0 <= loc_x < x and 0 <= loc_y < y and grid[loc_x][loc_y] == 1:
                    grid[loc_x][loc_y] = 2
                    stack.append((loc_x,loc_y,time+1))
        if any(1 in row for row in grid):
            return -1
        return time
    
