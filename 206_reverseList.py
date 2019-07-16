"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #recursion
        if head is None or head.next is None:
        	return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

        def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #iteratively
        prev, curr = None, head
        while curr is not None:
        	next_temp = curr.next
        	curr.next = prev
        	prev = curr
        	curr = next_temp
        return prev