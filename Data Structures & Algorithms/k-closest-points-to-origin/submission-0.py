class Solution:

    @staticmethod
    def euc_distance(x1, x2, y1, y2):
        # (sqrt((x1 - x2)^2 + (y1 - y2)^2))
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # simple solution: sort, return first k 
        return sorted(points, key=lambda p: self.euc_distance(0, p[0], 0, p[1]))[:k]