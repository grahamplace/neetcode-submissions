from _heapq import heappop
from heapq import heapify

class Solution:
    def _get_subsequence_of_num(self, nums_set: set[int], starting_from: int) -> list[int]:
        seq = [starting_from]
        curr = starting_from
        while True:
            pos_check = curr + 1
            if pos_check in nums_set:
                seq.append(pos_check)
                curr = pos_check
            else:
                break

        curr = starting_from
        while True:
            neg_check = curr - 1
            if neg_check in nums_set:
                seq.append(neg_check)
                curr = neg_check
            else:
                break
        
        return seq

    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # drop duplicates is fine

        longest_length = 0
        while len(nums_set) > 0:
            # "pop" first (any) number, find its max sequence by checking +-1 vals in both dirs
            curr_seq = self._get_subsequence_of_num(nums_set, next(iter(nums_set)))
            longest_length = max(longest_length, len(curr_seq))

            # remove all the values of this seq. one elem can be in at most one maximal length seq that we process to keep this O(n)
            for n in curr_seq:
                nums_set.remove(n)
        
        return longest_length
