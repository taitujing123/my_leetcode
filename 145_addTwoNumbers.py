"""
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。

 

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶:

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例:

输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        num1 = []
        num2 = []
        while l1 is not None:
            num1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            num2.append(l2.val)
            l2 = l2.next
        res = []
        curry = 0
        while len(num1) > 0 and len(num2) > 0:
            temp = num1.pop() + num2.pop() + curry
            res.append(temp % 10)
            curry = temp // 10
        while len(num1) > 0:
            temp = num1.pop() + curry
            res.append(temp % 10)
            curry = temp // 10
        while len(num2) > 0:
            temp = num2.pop() + curry
            res.append(temp % 10)
            curry = temp // 10
        if curry > 0:
            res.append(curry)
        dummy  = curr = ListNode(-1)
        while len(res) > 0:
            curr.next = ListNode(res.pop())
            curr = curr.next
            
        return dummy.next
            
        