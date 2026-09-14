"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
Want to know if ANY intervals overlap at all
end bounds touching start bounds of next != overlap

Idea:
Sort by start time:

[(0,30),(5,10),(15,20)]

if sorted by start, we can compare i to i + 1 pairs
if any overlap, return false early

O(nlogn) sort
O(n) compare pass 

O(nlogn) time 
O(1) auxillary space
'''

class Solution:

    def _do_intervals_overlap(self, a: Interval, b: Interval) -> bool:
        # should only call with a start <= b start 
        if a.start > b.start: 
            raise ValueError()
        
        # overlap if b.start < a.end
        if b.start < a.end:
            return True

        return False

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # quick tests 
        assert self._do_intervals_overlap(Interval(0, 10), Interval(0, 20)) == True
        assert self._do_intervals_overlap(Interval(0, 10), Interval(10, 20)) == False
        assert self._do_intervals_overlap(Interval(0, 10), Interval(12, 20)) == False
        assert self._do_intervals_overlap(Interval(0, 10), Interval(1, 2)) == True

        # sort intervals:
        intervals.sort(key=lambda x: (x.start, x.end)) # probably dont need to break ties with end?

        for i in range(len(intervals) - 1):
            if self._do_intervals_overlap(intervals[i], intervals[i + 1]):
                return False

        return True
