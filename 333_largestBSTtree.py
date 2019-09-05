"""
给定一个二叉树，找到其中最大的二叉搜索树（BST）子树，其中最大指的是子树节点数最多的。

注意:
子树必须包含其所有后代。

示例:

输入: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

输出: 3
解释: 高亮部分为最大的 BST 子树。
     返回值 3 在这个样例中为子树大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-bst-subtree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
        	return 0
        if root.left is None and root.right is None:
        	return 1
        if self.validBST(root):
        	return countNode(root)
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    def validBST(node):
    	def helper(node, small, large):
    		if node is None:
    			return True
    		if node.val >= large or node.val <= small:
    			return False
    		return helper(node.left, small, node.val) or helper(node.right, node.val, large)

    	return helper(root, float('-inf'), float('inf'))

    def countNode(node):
    	if node is None:
    		return 0
    	if node.left is None and node.right is None:
    		return 1
    	return self.countNode(node.left) + self.countNode(node.right) + 1