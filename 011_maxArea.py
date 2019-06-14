"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ls = len(height)
        lm = min(height[0], height[ls-1])
        max_v = lm * (ls - 1)
        low = 0
        high = ls - 1
        while low < high:
        	while height[low] < lm and low < ls:
        		low += 1
        	while height[high] < lm and high < ls:
        		high -= 1
        	if low > high:
        		break
        	m = min(height[low],height[high])
        	if m * (high - low) > max_v:
        		max_v = m * (high - low)
        		lm = m
        	if height[low] < height[high]:
        		low += 1
        	else:
        		high -= 1
        return max_v
