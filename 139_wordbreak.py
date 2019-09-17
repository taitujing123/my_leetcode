"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        r = False
        def help(s, d):
            nonlocal r
            if r or not s:
                r = True
                return True
            for w in d:
                if w == s[0:len(w)]:
                    help(s[len(w):], d)

        help(s, wordDict)
        return r
"""
class Solution:
    def wordBreak(self, s, wordDict):
        """
        1. 此题有点难度, 答案来自:
        https://leetcode.com/problems/word-break/discuss/43788/4-lines-in-Python
        2. dp问题: 针对s, dp[0~i] = dp[0~j] + dp[j~i], i = len(s)
        3. 我们将dp[0~j]存储到ok数组中, 避免重复判断.
        """
        ok = [True]
        for i in range(1, len(s) + 1):
            res = []
            for j in range(i):
                res.append(ok[j] and s[j:i] in wordDict)
            ok.append(any(res))
        return ok[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("applepenapple", ["apple", "pen"]))

