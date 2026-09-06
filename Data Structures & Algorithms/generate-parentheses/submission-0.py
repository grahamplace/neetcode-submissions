class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        def _explore(prefix: str, open_remaining: int, closed_remaining: int, solutions: list[str]):
            if open_remaining == 0 and closed_remaining == 0:
                solutions.append(prefix)
            
            if open_remaining > 0:
                _explore(prefix + "(", open_remaining - 1, closed_remaining, solutions)
            
            if closed_remaining > open_remaining:
                _explore(prefix + ")", open_remaining, closed_remaining - 1, solutions)
            
        solutions = []
        _explore("", n, n, solutions)
        return solutions
