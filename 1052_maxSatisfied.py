"""
这道题用一个大小为X的滑动窗口从数组customers的开始处往后移动，将窗口内的所有顾客以及窗口外所有的 grumpy[i]==0 的位置的顾客数相加，最后取所有结果中的最大值即可。

作者：1033020837
链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner/solution/hua-dong-chuang-kou-by-1033020837/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        n = len(customers)
        cur = 0
        for i in range(n):
            if i < X or grumpy[i] == 0:
                cur += customers[i]
        i = X
        ans = cur
        while i < n:
            if grumpy[i] == 1:
                cur += customers[i]
            if grumpy[i - X] == 1:
                cur -= customers[i-X]
            ans = max(ans,cur)
            i += 1
        return ans