class Solution:

    def _explore(self, options: list, i: int, path: list, solutions: list, k: int):

        if len(path) == k:
            solutions.append(list(path))
            return

        if i >= len(options):
            return

        for j in range(i, len(options)):
            path.append(options[j])
            self._explore(options, j + 1, path, solutions, k)    
            path.pop()


    def combine(self, n: int, k: int) -> List[List[int]]:
        options = list(range(1, n + 1))
        solutions = []
        self._explore(options, 0, [], solutions, k)
        return solutions