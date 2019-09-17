"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        self.sortList(head)
        self.sortList(mid)
        res = self.merge(head, mid)

        return res

    def merge(self, p1, p2):
        dummyHead = p = ListNode(-1)
        while p1 and p2:
            nex = p.next
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
        p.next = p1 if p1 else p2
        return dummyHead.next


if __name__ == '__main__':
    head = ListNode(4)
    node1 = ListNode(2)
    node2 = ListNode(1)
    node3 = ListNode(3)
    head.next = node1
    node1.next = node2
    node2.next = node3
    s = Solution()
    print(s.sortList(head))

