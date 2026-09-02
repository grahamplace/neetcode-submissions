
'''
[30,38,30,36,35,40,28]

stack:
(30, 0)
reach 38
38 > top of stack, i = 1
pop (30, 0)
set out[popidx] = i - popidx

stack 
(38, 1)
reach 30
(38, 1) (30, 2)
reach 36 
36 is > top of stack i = 3
pop (30, 2)
set out[popidx] = i - popidx

'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack:
                top = stack[-1]
                if temp > top[0]:
                    popped = stack.pop()
                    result[popped[1]] = idx - popped[1]
                else:
                    break
            
            stack.append((temp, idx))

        return result