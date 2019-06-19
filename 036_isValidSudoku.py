"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-sudoku
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        vset = [0] * 9
        hset = [0] * 9
        bset = [0] * 9
        for i in range(9):
        	for j in range(9):
        		curr = board[i][j]
        		if curr != '.':
        			index = 1 << (ord(curr) - ord('0'))
        			if (hset[i] & index) > 0 or (vset[j] & index) > 0 or (bset[(i / 3) * 3 + j / 3] & index) > 0:
        				return False
        			hset[i] |= index
        			vset[j] |= index
        			bset[(i/3)*3+j/3] |= index
        return True

 def isValidSudoku(self, board):
         if board is None:
             return True
         for i in range(9):
             table = {}
             for j in range(9):
                 curr = board[i][j]
                 if curr == '.':
                     continue
                 else:
                     try:
                         table[curr] += 1
                         return False
                     except KeyError:
                         table[curr] = 1
         for j in range(9):
             table = {}
             for i in range(9):
                 curr = board[i][j]
                 if curr == '.':
                     continue
                 else:
                     try:
                         table[curr] += 1
                         return False
                     except KeyError:
                         table[curr] = 1
         for i in range(3):
             for j in range(3):
                 table = {}
                 for k in range(9):
                     curr = board[i * 3 + k / 3][j * 3 + k % 3]
                     if curr == '.':
                         continue
                     else:
                         try:
                             table[curr] += 1
                             return False
                         except KeyError:
                             table[curr] = 1
         return True