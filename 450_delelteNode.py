"""
总的来讲，删除某一节点的情况有三种：

1.该节点无子节点：直接删除
2.该节点只有一个子节点：用对应的子树来代替该节点
3.该节点有两个字节点：用该节点的前驱节点或者后继节点来代替该节点
"""
方法一：用前驱结点（左子树中最大结点）代替被删除结点
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1：用左子树中最大结点的代替被删除结点


class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        if root.left is None:
            new_root = root.right
            root.right = None
            return new_root

        if root.right is None:
            new_root = root.left
            root.left = None
            return new_root

        # 找到左子树中最大的
        predecessor = self.__maximum(root.left)
        predecessor_copy = TreeNode(predecessor.val)
        predecessor_copy.left = self.__remove_max(root.left)
        predecessor_copy.right = root.right
        root.left = None
        root.right = None
        return predecessor_copy

    def __remove_max(self, node):
        if node.right is None:
            new_root = node.left
            node.left = None
            return new_root
        node.right = self.__remove_max(node.right)
        return node

    def __maximum(self, node):
        while node.right:
            node = node.right
        return node

方法二：用后继结点（右子树中最小结点）代替被删除结点
参考代码 2：

PythonJava
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法2：用右子树中最小结点的代替被删除结点

 def deleteNode(self, root, key):
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        if root.left is None:
            new_root = root.right
            root.right = None
            return new_root

        if root.right is None:
            new_root = root.left
            root.left = None
            return new_root

        # 找到右子树中最小的结点，复制它的值
        successor = self.__minimum(root.right)
        successor_copy = TreeNode(successor.val)
        successor_copy.left = root.left
        successor_copy.right = self.__remove_min(root.right)
        root.left = None
        root.right = None
        return successor_copy

    def __remove_min(self, node):
        if node.left is None:
            new_root = node.right
            node.right = None
            return new_root
        node.left = self.__remove_min(node.left)
        return node

    def __minimum(self, node):
        while node.left:
            node = node.left
        return node
