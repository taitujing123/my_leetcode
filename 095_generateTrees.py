"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
        	return []
        return self.get_trees(1, n)

    def get_trees(self, start, end):
    	#recursive solve the problem
    	res = []
    	if start > end:
    		res.append(None)
    		return res
    	for i in range(start, end + 1):
    		lefts = self.get_trees(start, i - 1)
    		rights = self.get_trees(i + 1, end)
    		for j in range(len(lefts)):
    			for k in range(len(rights)):
    				#root point
    				root = TreeNode(i)
    				root.left = lefts[j]
    				root.right = rights[k]
    				res.append(root)
    	return res
