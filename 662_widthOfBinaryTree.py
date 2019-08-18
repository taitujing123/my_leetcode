"""
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

示例 1:

输入:

           1
         /   \
        3     2
       / \     \
      5   3     9

输出: 4
解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
用一个队列记录某层的坐标和节点，下一个轮队列由这一轮队列的节点生成，首末元素的坐标差就是该层的最大宽度，相当于是宽搜。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        que = [[0, root]]  # 起始坐标为0，节点为根节点
        ans = 1
        while que:
            ans = max(ans, que[-1][0] - que[0][0] + 1)
            tmp = []  # 下一轮队列
            for i, q in que:
                if q.left:
                    tmp += [[i * 2, q.left]]  # 坐标节点生成
                if q.right:
                    tmp += [[i * 2 + 1, q.right]]
            que = tmp
        return ans
