"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #dummy head
        pos = dummyHead = ListNode(-1)
        while l1 is not None and l2 is not None:
        	if l1.val <= l2.val:
        		pos.next = l1
        		l1 = l1.next
        	else:
        		pos.next = l2
        		l2 = l2.next
        	pos = pos.next
       #merge resiual l1
        if l1 is not None:
        	pos.next = l1
        if l2 is not None:
        	pos.next = l2
        return dummyHead.next

