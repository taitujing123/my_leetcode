"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        #let permutations with first identical num be a block
        #target in (k-1) / (n-1): block
        remain = range(1, n + 1)
        if k <= 1:
        	return ''.join(str(t) for t in remain)
        total = 1
        for num in remain[:-1]:
        	total *= num
        res = self.do_getPermutation(remain, total, n - 1, k - 1)
        return ''.join(str(t) for t in res)

    def do_getPermutation(self, remain, curr, n, k):
    	if n == 0 or k <= 0 or curr == 0:
    		return remain
    	#which block
    	step = k / curr
    	# remain k value
    	k %= curr
    	curr /= n
    	res = [remain[step]] + self.do_getPermutation(remain[:step] + remain[step + 1:], curr, n - 1, k)
    	return res