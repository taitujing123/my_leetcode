"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3],

函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
        	return 0
        length = len(nums)
        result = 0
        i = j = 0
        while i < length:
        	j = i
        	while j < length:
        		if nums[j] != nums[i]:
        			break
        		j += 1
        	if j - i > 2:
        		length -= j - i - 2
        		for k in range(j - i - 2):
        			del nums[i]
        		result += 2
        		j = i + 2
        	else:
        		result += (j - i)
        	i = j
        return result
