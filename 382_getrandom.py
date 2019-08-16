"""
Reservoir sampling（水塘抽样）

题目1：

给出一个数据流，这个数据流的长度很大或者未知。并且对该数据流中数据只能访问一次。请写出一个随机选择算法，使得数据流中所有数据被选中的概率相等。

对于复杂问题一定要学会归纳总结，即从小例子入手，然后分析，得出结论，然后在证明。不然遇到一个抽象问题，不举例感觉这个问题，直接解还是比较难的。

对于此问题的难处就是数据流的长度未知，如果已知，so easy。现在进行归纳总结：

1） 长度为1，只有一个数据，直接返回即可，此数据被返回的概率为1.

2）长度为2，当读取第一数据时，我们发现并不是最后一个数据，我们不能直接返回，因为数据流还没结束，继续读取，到第二数据的时候，发现已经结束。所以现在的问题就是等概率返回其中的一个，显然概率为0.5。所以此时我们可以生成一个0到1的随机数p，如果p小于0.5，返回第二个，如果大于0.5，返回第一个。显然此时两个数据被返回的概率是一样的。

3）长度为3，我们可以事先分析得到，为了满足题意，需要保证每个数据返回的概率都是1/3。接下来分析数据流，首先读取第一个数据，然后在读取第二个数据，此时可以按2）处理，保留一个数据，每个数据显然为1/2。此时读取第三个数据，发现到尾部了，为了满足题意，此时需要一1/3的概率决定是否取此数据。现在分析前两个数是否也是以1/3的概率返回，如果是则总体都满足。数据1和数据2同时留下的概率为：1/2 *（1-1/3）= 1/3。1/2只在数据1和数据2pk时，能留下的概率，1-1/3指数据3不被留下的概率。所以，对长度为3的数据流，在读取第三个数据时，我们可以生成一个0到1的随机数p，如果p小于1/3，返回第三个数据，否则，返回前面两个pk留下的数据。

由上面的分析，我们可以得出结论，在取第n个数据的时候，我们生成一个0到1的随机数p，如果p小于1/n，保留第n个数。大于1/n，继续保留前面的数。直到数据流结束，返回此数。

下面用数学归纳法证明此结论。

1)当n=1时，第一个元素以1/1的概率返回，符合条件。

2)假设当n=k时成立，即每个元素都以1/k的概率返回，先证明n=k+1时，是否成立。

对于最后一个元素显然以1/k+1的概率返回，符合条件，对于前k个数据，被返回的概率为1/k * (1- 1/k+1)=1/k+1，满足题意。

综上所述，结论成立。

题目2

对于题目1的要就变为，最后返回的结果长度为k，这就是水塘抽样

显然有了对题目1的理解，我们可以直接替换结论，只需把上面的1/n变为k/n即可。

在取第n个数据的时候，我们生成一个0到1的随机数p，如果p小于k/n，替换池中任意一个为第n个数。大于k/n，继续保留前面的数。直到数据流结束，返回此k个数。但是为了保证计算机计算分数额准确性，一般是生成一个0到n的随机数，跟k相比，道理是一样的。

给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。

进阶:
如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-random-node
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from random import random


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        count, res = 1, -1
        cur = self.head
        while cur:
            if int(random() * count) == 0:
                res = cur.val
            count, cur = count + 1, cur.next
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()