'''
input:
[1,2,3],[7,1,1]

Want:
[7,2,3]

Can do merge() on any pair of triplets in input, as many times as we want
- take the max of each position
- merge([1,2,3],[7,1,1]) = [7, 2, 3]. Answer = yes

We can't just ask "is the target value present in any triplet" 
- because the merge might blow away our ability to reach target in some position 
e.g. 
[2,5,6],[1,4,4],[5,7,5], target [5,4,6]

in general I think we might do something like sort on A values, merge until target is reached. if not reached, return
then merge on B, etc

Naive solution
O(n) first pass. if target values not all present, return False early

Then, sort by a, b, c order
[2,5,6],[1,4,4],[5,7,5]
-> 
[1,4,4],[2,5,6],[5,7,5]
Then, merge to compress until 1 elem
We can stop if any new compressed elem has any element > target


[2,5,3],[1,8,4],[1,7,5], target: [2,7,5]
[1,7,5],[1,8,4],[2,5,3]
[1,8,5],[2,5,3]
[2,8,5]


[2,5,3],[1,8,4],[1,7,5]

maybe more like a decision tree problem
start at first elem. take or skip 
move to next elem, take or skip 
take here means merge w previous 
We should always skip any time a value is "invalid" any elem above any target elem
'''

class Solution:
    
    def is_valid_candidate(self, triplet: List[int], target: List[int]) -> bool:
        for i in range(len(target)):
            if triplet[i] > target[i]:
                return False
        return True

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets = [t for t in triplets if self.is_valid_candidate(t, target)]

        a_pres, b_pres, c_pres = False, False, False
        for triplet in triplets:
            if triplet[0] == target[0]:
                a_pres = True
            if triplet[1] == target[1]:
                b_pres = True
            if triplet[2] == target[2]:
                c_pres = True
        
        return all([a_pres, b_pres, c_pres ])






