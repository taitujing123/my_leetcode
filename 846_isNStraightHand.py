"""
爱丽丝有一手（hand）由整数数组给定的牌。 

现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。

如果她可以完成分组就返回 true，否则返回 false。

 

示例 1：

输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
输出：true
解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
示例 2：

输入：hand = [1,2,3,4,5], W = 4
输出：false
解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hand-of-straights
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        length = len(hand)
        #如果无法整除则直接返回false
        if length % W != 0:
        	return false
        hand_counter = dict()

        for i in range(length):
        	hand_counter[hand[i]] = hand_counter.get(hand[i], 0) + 1

        sort_hand = sorted(hand_counter)

        for h in sort_hand:
        	if hand_counter[h] == 0:
        		continue
        	elif hand_counter[h] < 0:
        		return False 
        	else:
        		for i in range(1,W):
        			if hand_counter.get(h+i, 0) == 0:
        				return False
        			else:
        				hand_counter[h+i] -= hand_counter[h]

        return True





