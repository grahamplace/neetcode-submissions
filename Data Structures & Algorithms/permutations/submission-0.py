class Solution:
    def explore(self, choices: set[int], path: list[int], solutions: list[list[int]]) -> None:
        print(choices, path)
        # base case, we have no more choices, flush that path to solutions
        if len(choices) == 0:
            solutions.append(list(path))
            return 
        
        # otherwise, make a choice and continue exploring
        for choice in list(choices):
            choices.remove(choice)
            path.append(choice)
            self.explore(choices, path, solutions)
            path.pop()
            choices.add(choice)


    def permute(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        self.explore(set(nums), [], solutions)
        return solutions
        
        