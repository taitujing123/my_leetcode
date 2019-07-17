"""
对链表进行插入排序。
插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insertion-sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
        	return head

        dummy = ListNode(-1)
        dummy.next = head
        pre = head #始终指向排序好的链表的最后一个节点
        cur = head.next #始终指向未排序的第一个节点
        while cur:
        	tail = cur.next
        	pre.next = tail #把cur节点取出来

        	p = dummy
        	while p.next and p.next.val < curr.val:
        		p = p.next
        	cur.next = p.next #找到插入的位置，把cur插入到p和p.next之间
        	p.next = cur
        	cur = tail

        	if p == pre: #如果刚刚插入到已排序的链尾
        		pre = pre.next
        return dummy.next
        
