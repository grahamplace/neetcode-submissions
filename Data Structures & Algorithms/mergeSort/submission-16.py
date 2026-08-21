from typing import List

class Solution:
    @staticmethod
    def _print_pairs(pairs: List[Pair]) -> None:
        print([(p.key, p.value) for p in pairs])

    @staticmethod
    def _merge_arrays(left: List[Pair], right: List[Pair]) -> List[Pair]:
        i = 0
        j = 0

        merged: List[Pair] = []
        while (i < len(left) and j < len(right)):
            curr_i = left[i]
            curr_j = right[j]

            if curr_i.key <= curr_j.key:
                merged.append(curr_i)
                i += 1
            else: 
                merged.append(curr_j)
                j += 1
        
        # we exit while loop when left or right is fully merged
        # we still need to merge remainder of non-fully-merged array 
        if i < len(left):
            merged.extend(left[i:])
        else:
            merged.extend(right[j:])

        return merged

    def _merge_sort(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:
        # base case == single elem array which is necessarily sorted
        if len(pairs) == 0: 
            return []

        if start == end - 1:
            return [pairs[start]]

        pivot = start + ((end - start) // 2)
        print(f"Pivot: {pivot}")

        left = self._merge_sort(pairs, start, pivot)
        print("Left: ")
        self._print_pairs(left)

        right = self._merge_sort(pairs, pivot, end)
        print("Right: ")
        self._print_pairs(right)

        return self._merge_arrays(left, right)

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if (len(pairs) == 0):
            return []

        return self._merge_sort(pairs, 0, len(pairs))