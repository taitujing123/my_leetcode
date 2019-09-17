"""
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。

如果不含有 “山脉” 则返回 0。

 

示例 1：

输入：[2,1,4,7,3,2,5]
输出：5
解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
示例 2：

输入：[2,2,2]
输出：0
解释：不含 “山脉”。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-mountain-in-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution1(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ls = len(A)
        if ls < 3:
            return 0
        dp = [[False for _ in range(ls)] for _ in range(ls)]
        for i in range(ls - 2):
            if A[i] < A[i + 1] and A[i + 2] < A[i + 1]:
                dp[i][i + 2] = True

        for r in range(3, ls - 1):
            for l in range(r - 1):
                if A[r + 1] < A[r] and dp[l][r] and r - l >= 2:
                    dp[l][r + 1] = True

        for r in reversed(range(3, ls)):
            for l in reversed(range(1, r - 1)):
                if A[l - 1] < A[l] and dp[l][r] and r - l >= 2:
                    dp[l - 1][r] = True

        res = 0
        for i in range(ls):
            for j in range(ls):
                if dp[i][j] and j - i + 1 > res:
                    res = j - i + 1

        return res


class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(A):
            j = i
            # 找到上升的终点，即山顶
            while j + 1 < len(A) and A[j] < A[j + 1]:
                j += 1
            mid = j
            # 找到下降的终点
            while j + 1 < len(A) and A[j] > A[j + 1]:
                j += 1
            # 判断是否构成山脉
            if i < mid < j:
                res = max(res, j - i + 1)
            # 如果是平山，i后移一位，否则下降的终点作为新的起点
            if i == j:
                i += 1
            else:
                i = j
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestMountain([2,1,4,7,3,2,5]))
