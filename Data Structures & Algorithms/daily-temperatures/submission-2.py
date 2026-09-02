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