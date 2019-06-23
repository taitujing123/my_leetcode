"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs.sort()
        hash = {}
        for s in strs:
        	key = self.hash_key(s)
        	try:
        		hash[key].append(s)
        	except KeyError:
        		hash[key] = [s]
        return hash.values()
    def hash_key(self, s):
    	#hash string with 26 length array
    	table = [0] * 26
    	for ch in s:
    		index = ord(ch) - ord('a')
    		table[index] += 1
    	return str(table)
