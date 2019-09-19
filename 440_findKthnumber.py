"""
给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

注意：1 ≤ k ≤ n ≤ 109。

示例 :

输入:
n: 13   k: 2

输出:
10

解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        str_n = [str(i + 1) for i in range(n)]
        l, r = 0, len(str_n) - 1
        while l < r:
            p = self.paration(str_n, l, r)
            if p == k - 1:
                return int(str_n[p])
            elif p < k - 1:
                l = p + 1
            else:
                r = p - 1

    def paration(self, arr, l, r):
        pivot = arr[r]
        i = l - 1
        for j in range(l, r):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1