"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True] * n
        for i in range(2, n):
        	if i * i > n:
        		break
        	if not isPrime[i]:
        		continue
        	for j in range(i*i, n, i):
        		isPrime[j] = False
        count = 0
        for i in range(2, n):
        	if  isPrime[i]:
        		count += 1
        return count