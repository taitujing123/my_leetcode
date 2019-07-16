 """
 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 """
 def findKthLargest(self, nums, k):
        # shuffle nums to avoid n*n
        random.shuffle(nums)
        return self.quickSelection(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelection(self, nums, start, end, k):
        if start > end:
            return float('inf')
        pivot = nums[end]
        left = start
        for i in range(start, end):
            if nums[i] <= pivot:
                # swip left and i
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        nums[left], nums[end] = nums[end], nums[left]
        if left == k:
            return nums[left]
        elif left < k:
            return self.quickSelection(nums, left + 1, end, k)
        else:
            return self.quickSelection(nums, start, left - 1, k)