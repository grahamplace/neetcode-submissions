# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        # base case, single element array (or empty), it's already sorted
        if len(pairs) <= 1:
            return pairs

        """
        basic idea:
        pick pivot value
        [2, 1, 4, 3*]

        iterate across list O(n)
        we want to partition into two lists:
         - left = all elems <= pivot
         - right = all elems > pivot 

        we can do this in place by swapping, we don't need to allocate left and right arrays
        
        then put the pivot at the end of left (since everything in left is <= pivot value)

        [5, 3, 1]

        these are NOT sorted yet, then we recursively sort each partition
         - excl the pivot point

        
        """

        leftRegionEnd = 0
        pivotIdx = len(pairs) - 1
        pivot = pairs[pivotIdx]
        pivotVal = pivot.key

        for i in range(len(pairs) - 1):
            curr = pairs[i]
            if curr.key >= pivotVal:
                pass
            else:  # SWAP left and i
                tmp = pairs[i]
                pairs[i] = pairs[leftRegionEnd]
                pairs[leftRegionEnd] = tmp
                leftRegionEnd += 1
            
        
        # last, always swap pivot and final L

        pairs[pivotIdx] = pairs[leftRegionEnd]
        pairs[leftRegionEnd] = pivot
            
        print("leftRegionEnd", leftRegionEnd)
        return (
            self.quickSort(pairs[:leftRegionEnd]) + 
            [pairs[leftRegionEnd]] + 
            self.quickSort(pairs[leftRegionEnd + 1:])
        )



        # quicksort is in place, so we should aim to return the passed in list
        return pairs
