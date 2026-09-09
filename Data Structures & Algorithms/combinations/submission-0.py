class Solution:

    def _explore(self, options: list, i: int, path: list, solutions: list, k: int):

        if len(path) == k:
            solutions.append(list(path))
            return

        if i >= len(options):
            return


        for j in range(i, len(options)):
            # choose
            path.append(options[j])
            # explore
            self._explore(options, j + 1, path, solutions, k)    
            # unchoose
            path.pop()

        # ### skip this one
        # self._explore(options, i + 1, path, solutions)
        
        # ### take this one

        # # choose
        # path.append(options[i])

        # # explore
        # self._explore(options, i + 1, path, solutions)
        # # unchoose
        # path.pop()


    def combine(self, n: int, k: int) -> List[List[int]]:
        options = list(range(1, n + 1))
        solutions = []
        self._explore(options, 0, [], solutions, k)
        return solutions