"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ls = len(height)
        if ls == 0:
        	return 0 
        res, left = 0, 0
        while left < ls and height[left] == 0:
        	left += 1
        pos = left + 1
        while pos < ls:
        	if height[pos] >= height[left]:
        		#there is a right bar which is no less than left bar
        		res += self.rain_water(height, left, pos)
        		left = pos
        		pos += 1
        	elif pos == ls - 1:
        		#left bar is higher than all right bar
        		max_value, max_index = 0, pos
        		for index in range(left + 1, ls):
        			if height[index] > max_value:
        				max_value = height[index]
        				max_index = index
        		res += self.rain_water(height, left, max_index)
        		left = max_index
        		pos = left + 1
        	else:
        		pos += 1
        return res

    def rain_water(self, height, start, end):
        # computer rain water
        if end - start <= 1:
            return 0
        min_m = min(height[start], height[end])
        res = min_m * (end - start - 1)
        step = 0
        for index in range(start + 1, end):
            if height[index] > 0:
                step += height[index]
        return res - step
