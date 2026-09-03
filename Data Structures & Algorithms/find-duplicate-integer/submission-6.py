
'''
Solve without modifying the array nums and using O(1) extra space?

key: Each integer in nums is in the range [1, n] inclusive.
- aka each VALUE is an index of the array
- so we can treat it more like a linked list / graph
- and we are talking about CYCLE detection
== fast and slow pointer


1SF,2,3,2,2
-> send each ptr to index val, do that 2x for fast
a. 1,2SF,3,2,2
b. 1,2S,3F,2,2

a. 1,2,3S,2F,2
b. 1,2F,3S,2,2

a. 1,2,3F,2S,2
b. 1,2,3,2SF,2 * when fast / slow intersect, cycle is detected

algo for finding the head of cycle is basically
when F/S intersect, slow2 = head
iterate slow and slow2 until they intersect, that is head of cycle
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # naive:
        # return Counter(nums).most_common(1)[0][0]

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast] # 2x for fast

            if slow == fast:
                break
        
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow

