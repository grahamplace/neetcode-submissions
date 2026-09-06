class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        def _explore(stack: list[str], open_used: int, closed_used: int, solutions: list[str]):
            if open_used == n and closed_used == n:
                solutions.append("".join(stack))
                return
            
            if open_used < n:
                stack.append("(")
                _explore(stack, open_used + 1, closed_used, solutions)
                stack.pop()
            
            if closed_used < n and closed_used < open_used:
                stack.append(")")
                _explore(stack, open_used, closed_used + 1, solutions)
                stack.pop()


        solutions = []
        _explore([], 0, 0, solutions)
        return solutions
