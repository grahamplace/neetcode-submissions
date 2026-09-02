class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sums = [0] * len(nums)
        prev = 0
        for i in range(len(nums)):
            self.prefix_sums[i] = prev
            prev += nums[i]

    def sumRange(self, left: int, right: int) -> int:
        total_incl_right = self.prefix_sums[right] + self.nums[right]
        return total_incl_right - self.prefix_sums[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)