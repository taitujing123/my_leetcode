"""
在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。

一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：

相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
C_1 位于 (0, 0)（即，值为 grid[0][0]）
C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-path-in-binary-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]
        if n==1 and m==1:
            return 1
        if grid[0][0]==1 or grid[n-1][m-1]==1:
            return -1
        x=[-1,-1,-1, 0, 0, 1, 1, 1]
        y=[-1, 0, 1,-1, 1,-1, 0, 1]
        stack=[(0,0)]
        visited[0][0]=1
        step=1
        temp_list=[]
        while len(stack):
            cur_x,cur_y=stack.pop()
            step=visited[cur_x][cur_y]
            step+=1
            for i in range(8):
                next_x,next_y=cur_x+x[i],cur_y+y[i]
                if next_x==n-1 and next_y==m-1:
                    return step
                if 0<=next_x<=n-1 and 0<=next_y<=m-1 and grid[next_x][next_y]==0 and visited[next_x][next_y]==0:
                    temp_list.append((next_x,next_y))
                    visited[next_x][next_y]=step
                else:
                    continue
            if len(stack)==0:
                stack=temp_list.copy()
                temp_list=[]

        return -1