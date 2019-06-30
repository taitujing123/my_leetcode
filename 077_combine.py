"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.get_combine(res, [], n, k, 1)
        return res
    
    def get_combine(self, res, prefix, n, k, start):
        #recursive with only one array
        if k == 0:
            res.append(list(prefix))
        elif start <= n:
            prefix.append(start)
            self.get_combine(res, prefix, n, k - 1, start + 1)
            prefix.pop()
            self.get_combine(res, prefix, n, k, start + 1)
        
