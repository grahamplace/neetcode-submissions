from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = Counter(students)
        for s in sandwiches:
            if c[s] == 0:
                break
            else:
                c[s] -= 1
            
        return c[0] + c[1]
