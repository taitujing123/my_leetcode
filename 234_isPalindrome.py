"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        # p2 is 2 times faster than p3
        # p1 and pre is used to reverse the first half of the list
        # so when the first while is over
        # p1 is in the middle
        # p3 is in middle + 1
        # p2 is in the end
        if head is None:
            return True
        p1, p2 = head, head
        p3, pre = p1.next, p1
        while p2.next is not None and p2.next.next is not None:
            p2 = p2.next.next
            pre = p1
            p1 = p3
            p3 = p3.next
            p1.next = pre
        if p2.next is None:
            p1 = p1.next

        while p3 is not None:
            if p1.val != p3.val:
                return False
            p1 = p1.next
            p3 = p3.next
        return True
