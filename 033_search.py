"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search
        # if start < mid, then left part is sorted
        # if mid < end, then right part is sorted
        def get(start, end):
          if start > end:
            return -1
          mid = (start + end) / 2
          if nums[mid] == target:
            return mid
          elif nums[mid] >= nums[start]: # First half is sorted
            if target >= nums[start] and target < nums[mid]:
              return get(start, mid - 1)
            else:
              return get(mid + 1, end)
          elif nums[mid] <= nums[end]: # Second half is sorted
            if target > nums[mid] and target <= nums[end]:
              return get(mid + 1, end)
            else:
              return get(start, mid - 1)
        return get(0, len(nums) - 1)
        