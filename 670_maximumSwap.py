"""
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-swap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def maximumSwap(self, num: int):
        '''
        若最高位数字不是最大，则将其余位中的最大数字与最高位交换。
            若其余位中的最大数字不止一个，则将位数最低的那个与最高位交换。
        若最高位数字是最大，则对除去最高位的剩余数字进行递归操作。
        '''
        s, a = str(num), []
        for val in s:
            a.append(int(val))
        b = sorted(a, reverse = True)
        if a == b:
            return num
        i, l = 0, len(a)
        while i < l:
            if a[i] == b[i]:
                i += 1
            else:break
        for j in range(l-1, -1, -1):
            if a[j] == b[i]:
                a[j] = a[i]
                a[i] = b[i]
                break
        s = ''
        for x in a:
            s += str(x)
        return int(s)