"""
按照 开始时间 对会议进行排序。
初始化一个新的 最小堆，将第一个会议的结束时间加入到堆中。我们只需要记录会议的结束时间，告诉我们什么时候房间会空。
对每个会议，检查堆的最小元素（即堆顶部的房间）是否空闲。
若房间空闲，则从堆顶拿出该元素，将其改为我们处理的会议的结束时间，加回到堆中。
若房间不空闲。开新房间，并加入到堆中。
处理完所有会议后，堆的大小即为开的房间数量。这就是容纳这些会议需要的最小房间数。

作者：LeetCode
链接：https://leetcode-cn.com/problems/meeting-rooms-ii/solution/hui-yi-shi-ii-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
import heapq

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x.start)

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0].end)

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i.start:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i.end)

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

class Solution(object):
    def minMeetingRooms(self, intervals):
    	"""
    	intervals: List[List[int]]
    	"""
        I = intervals
        I.sort()
        sched=[]
        for s,e in I:
            assigned=False
            for rm in sched:
                if rm[-1][1]<=s:
                    rm.append((s,e))
                    assigned=True
                    break
            if not assigned:
                sched.append([(s,e)])
        return len(sched)