"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
        	return None
        slow = fast = head
        for i in range(n):
        	fast = fast.next
        if fast is None:
        	head = head.next
        	return head
        while fast.next is not None:
        	fast = fast.next
        	slow = slow.next
        curr = slow.next
        slow.next = curr.next
        return head