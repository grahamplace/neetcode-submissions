class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # naive, nested loop n^2, for each elem check all other elems for compliment
        for i, v_i in enumerate(nums):
            for j, v_j in enumerate(nums):
                if i == j: continue
                elif v_i + v_j == target:
                    return [min(i, j), max(i, j)]

        assert False, "should never be reached"

        # better: sort O(nlogn)
        # [3,4,5,6] -> [3,4,5,6]
