"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def get(start, end):
            if start > end:
                return False
            mid = (start + end) / 2
            # handle duplicate
            while mid < end and nums[mid + 1] == nums[mid]:
                mid += 1
            while start < mid and nums[start + 1] == nums[start]:
                start += 1
            if nums[mid] == target:
                return True
            elif mid == end:
                return get(start, mid - 1)
            elif start == mid:
                return get(mid + 1, end)
            elif nums[mid] >= nums[start]:
                # First half is sorted
                if target >= nums[start] and target < nums[mid]:
                    return get(start, mid - 1)
                else:
                    return get(mid + 1, end)
            elif nums[mid] <= nums[end]:
                # Second half is sorted
                if target > nums[mid] and target <= nums[end]:
                    return get(mid + 1, end)
                else:
                    return get(start, mid - 1)
        return get(0, len(nums) - 1)