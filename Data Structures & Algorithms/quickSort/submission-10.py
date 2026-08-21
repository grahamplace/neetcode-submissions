# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        # quickSort aka pivotSort

        # base case: empty or single array 
        if len(pairs) <= 1:
            return pairs
        
        left = 0
        pivot = pairs[-1]
        for i in range(len(pairs) - 1):
            curr = pairs[i]
            
            # swap curr and left pivot:
            if curr.key < pivot.key:
                pairs[i] = pairs[left]
                pairs[left] = curr
                left += 1
                
        
        # last, always swap pivot into position between two partitions:
        pairs[-1] = pairs[left]
        pairs[left] = pivot
        

        return (
            self.quickSort(pairs[:left]) +
            [pairs[left]] + 
            self.quickSort(pairs[left + 1:])
        )
        
        # in place sort, so return input, now sorted
        return pairs
