'''
[[1,3],[1,5],[6,7]]
- merge all overlapping intervals
- return an array of the non-overlapping intervals that cover all the intervals in the input

[[1,3],[1,5],[6,7]]
-> first two overlap and merge
-> [[1,5],[6,7]]

- sort by start time
[[1,3],[1,5],[6,7]]

- iterate over interval pairs
[1,3],[1,5]

- if overlap, merge

- continue iterating from there
'''
class Solution:
    def do_intervals_overlap(self, a: list[int], b: list[int]) -> bool:
        assert a[0] <= b[0] # we expect to only call this with start-ordered pairs
        return b[0] <= a[1]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return intervals

        # quick tests
        # assert self.do_intervals_overlap([0, 1], [2, 10]) == False
        # assert self.do_intervals_overlap([0, 1], [1, 2]) == True # end/start = do overlap
        # assert self.do_intervals_overlap([0, 5], [2, 3]) == True # fully contained B
        # assert self.do_intervals_overlap([0, 5], [2, 10]) == True # B extendes beyond a

        intervals.sort(key=lambda x: x[0])

        output = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            candidate = intervals[i]
            if self.do_intervals_overlap(curr, candidate): # merge
                curr[1] = max(curr[1], candidate[1]) # merge using the later end time
            else:
                # flush current to output
                output.append(curr)

                # reset curr to new candidate (possible to merge with next)
                curr = candidate

        # always flush last curr
        output.append(curr)

        return output







