"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
        	return head
        dummy_head = ListNode(-1)
        dummy_head.next = head
        slow = dummy_head
        fast = dummy_head.next
        while fast:
        	while fast.next and fast.next.val == slow.next.val:
        		fast = fast.next
        	if slow.next == fast:
        		slow = fast
        		fast = fast.next
        	else:
        		slow.next = fast
        		slow = fast
        		fast = fast.next
        return dummy_head.next
