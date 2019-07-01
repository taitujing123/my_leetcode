"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        check_board = [[True] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
        	for j in range(len(board[0])):
        		if board[i][j] == word[0] and check_board:
        			check_board[i][j] = False
        			res = self.check_exist(check_board, board, word, 1, len(word), i, j)
        			if res:
        				return True
        			check_board[i][j] = True
        return False

    def check_exist(self, check_board, board, word, index, ls, row, col):
    	if index == ls:
    		return True
    	for temp in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    		curr_row = row + temp[0]
    		curr_col = col + temp[1]
    		if curr_row >= 0 and curr_row < len(board) and curr_col >= 0 and curr_col < len(board[0]):
    			if check_board[curr_row][curr_col] and board[curr_row][curr_col] == word[index]:
    				check_board[curr_row][curr_col] = False
    				res = self.check_exist(check_board, board, word, index + 1, len(word), curr_row, curr_col)
    				if res:
    					return res
    				check_board[curr_row][curr_col] = True
    	return False
