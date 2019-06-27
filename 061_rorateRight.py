"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        slow = fast = head
        length = 1

        while k and fast.next:
            fast = fast.next
            length += 1
            k -= 1

        if k != 0:
            k = (k + length - 1) % length # original k % length
            return self.rotateRight(head, k)
        else:
            while fast.next:
                fast = fast.next
                slow = slow.next
            return self.rotate(head, fast, slow)

    def rotate(self, head, fast, slow):
        fast.next = head
        head = slow.next
        slow.next = None
        return head
