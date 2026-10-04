from collections import deque 
'''
{
    'a': {'b'}
}
{
    'a': 1
}
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [i for i in range(numCourses)]
        in_degrees = defaultdict(int)
        deps = defaultdict(set)
        for p in prerequisites:
            in_degrees[p[0]] += 1
            deps[p[1]].add(p[0])

        completed = 0 
        q = deque()
        for course_id in courses:
            if in_degrees[course_id] == 0:
                q.append(course_id)

        while q:
            curr = q.popleft()
            completed += 1
            for descendent in deps[curr]:
                in_degrees[descendent] -= 1
                if in_degrees[descendent] == 0:
                    q.append(descendent)
        
        return completed == numCourses
            
            
