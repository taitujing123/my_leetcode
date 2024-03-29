"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        less = lesshead = None
        last = pos = head
        while pos is not None:
            if pos.val < x:
                if lesshead is None:
                    lesshead = pos
                else:
                    less.next = pos
                less = pos
                if head == pos:
                    last = head = pos.next
                else:
                    last.next = pos.next
            else:
                last = pos
            pos = pos.next
        if lesshead is not None:
            less.next = head
        else:
            lesshead = head
        return lesshead


