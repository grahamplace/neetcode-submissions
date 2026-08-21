from typing import List
class Solution:
    def _is_int(self, s: str) -> bool:
        try:
            int(s)
            return True
        except:
            return False
            
    def calPoints(self, operations: List[str]) -> int:
        stack: List[int] = []

        for op in operations:
            print("current stack:", stack)
            print("current op:", op)
            if self._is_int(op):
                stack.append(int(op))
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()
            
        return sum(stack)