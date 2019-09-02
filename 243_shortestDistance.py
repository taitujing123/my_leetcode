"""
给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"]

输入: word1 = “coding”, word2 = “practice”
输出: 3
输入: word1 = "makes", word2 = "coding"
输出: 1
注意:
你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-word-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos1 = []
        pos2 = []
        for i in range(len(words)):
            if words[i] == word1:
                pos1.append(i)
            elif words[i] == word2:
                pos2.append(i)
        
        mindis = len(words)
        for i in range(len(pos1)):
            for j in range(len(pos2)):
                if abs(pos1[i]-pos2[j]) < mindis:
                    mindis = abs(pos1[i]-pos2[j])
        
        return mindis
#O(n)解法
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos1 = -1
        pos2 = -1
        mindis = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                pos1 = i
            elif words[i] == word2:
                pos2 = i
            
            if pos1 != -1 and pos2 != -1:
                mindis = min(mindis,abs(pos1-pos2))
        
        return mindis