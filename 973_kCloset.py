"""
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

 

示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释： 
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-closest-points-to-origin
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random
class Solution(Object):
	def kCloset(self, points, K):
		"""
		:type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
		"""
		dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2

		def work(i,j,k):
			if i >= j:
				return
			oi, oj = i, j
			pivot = dist(random.randint(i,j))
			while i < j:
				while i < j and dist(i) < pivot: i += 1
				while i < j and dist(j) > pivot: j -= 1
				points[i], points[j] = points[j], points[i]

			if K <= oi - i + 1:
				work(oi, i, k)
			else:
				work(i+1, oj, K - (i-oi+1))

		work(0, len(points)-1, K)
		return points[:K]