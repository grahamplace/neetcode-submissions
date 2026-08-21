class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        inputs are sorted in non-decreasing order
        m is the number of valid elements in nums1,
        n is the number of elements in nums2.
        array nums1 has a total length of (m+n), the last n elements set to 0 as placeholders

        shift_val = 2 
        [10,20,20,40*,0,0]
        [1,2*]

        [10,20,20*,0,0,40]
        [1,2*]

        [10,20,0*,0,20,40]
        [1,2*]

        ... etc

        [0,0*,10,20,20,40]
        [1,2*]

        if nums2[j] > nums1[i]: 
            nums1[i] = nums2[j]
            decr both pointers
            shift val -= 1


        [0*,2,10,20,20,40]
        [1*,2]

        [1, 3*, 0, 0]
        [2, 2*]

        [1, 0, 0, 3]
        [2, 2*]

        [1, 0, 0, 3]
        [2, 2*]
        """
        print(nums1)
        print(nums2)
        i = m - 1  # nums1 pointer starts at largest nums1
        j = len(nums2) - 1  # nums2 pointer starts at end of nums2
        shift_val = n

        while j >= 0:
            print(f"i: {i}, j: {j}, shift: {shift_val} nums1: {nums1}, nums2: {nums2}")
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[i + shift_val] = nums1[i]
                nums1[i] = 0
                i -= 1
            else: 
                nums1[i + shift_val] = nums2[j]
                shift_val -= 1
                j -= 1

        return
