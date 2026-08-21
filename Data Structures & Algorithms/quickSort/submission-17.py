# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def _quick_sort(self, pairs, start, end) -> List[Pair]:
        # want: [left], pivot, [right]
        # left is all values <= pivot
        # right is all values > pivot
        # recursively sort each and combine w/ pivot + return

        # Base Case: single elem array (necessarily already sorted)
        if start == end - 1:
            return [pairs[start]]
        elif start > end - 1:
            return []

        # Partition step
        # simple pivot pick = rightmost value
        pivot = pairs[end - 1]


        left = start
        for i in range(start, end-1):
            if pairs[i].key < pivot.key:
                tmp = pairs[i]
                pairs[i] = pairs[left]
                pairs[left] = tmp
                left += 1
        
        # always swap pivot, left at the end:
        tmp = pairs[left]
        pairs[left] = pivot
        pairs[end - 1] = tmp


        # Merge step
        # simple: [...left_sorted, pivot, ...right_sorted]
        return (
            self._quick_sort(pairs, start, left) + 
            [pivot] + 
            self._quick_sort(pairs, left + 1, end)
        )

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) == 0:
            return []

        return self._quick_sort(pairs, 0, len(pairs))
