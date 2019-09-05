"""
给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。

形式上，斐波那契式序列是一个非负整数列表 F，且满足：

0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
F.length >= 3；
对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。

返回从 S 拆分出来的所有斐波那契式的序列块，如果不能拆分则返回 []。

示例 1：

输入："123456579"
输出：[123,456,579]
示例 2：

输入: "11235813"
输出: [1,1,2,3,5,8,13]
示例 3：

输入: "112358130"
输出: []
解释: 这项任务无法完成。
示例 4：

输入："0123"
输出：[]
解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
示例 5：

输入: "1101111"
输出: [110, 1, 111]
解释: 输出 [11,0,11,11] 也同样被接受。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
	def splitIntoFibonacci(self, S):
		"""
		type S: str
		rtype: List[int]
		"""
		if S is None:
			return []
		res = []
		n = len(S)

		def helper(S, res, idx):
			# 终止条件,说明遍历整个字符串
			if idx == n and len(res) >= 3:
				return True

			for i in range(idx, n):
				# 当开头为"0"并且不止一位数的时候
				if S[idx] == "0" and i > idx:
					break
				
				num = int(S[idx:i + 1])
				tmp_n = len(res)
				# 不能超过最大整数
				if num > 2147483647:
					break
				# 前面两个数之和大于现在这个数
				if tmp_n >= 2 and num > res[-1] + res[-2]:
					break
				if tmp_n <= 1 or num == res[-1] + res[-2]:
					res.append(num)
					if helper(S, res, i + 1):
						return True
					res.pop()
			return False
        helper(S, res, 0)
        return res