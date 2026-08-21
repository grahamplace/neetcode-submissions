from collections import deque 

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        
        assert len(students) == len(sandwiches)

        rejectCounter = 0
        sandwich_idx = 0
        while True:
            student = q.popleft()
            if student == sandwiches[sandwich_idx]:
                sandwich_idx += 1
                rejectCounter = 0
            else:
                q.append(student)
                rejectCounter += 1
            
            if rejectCounter == len(q):
                return rejectCounter
            
            if len(students) == 0:
                return 0
            

    