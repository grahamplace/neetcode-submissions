from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small_numbers: list[int] = [] # MAX HEAP, values inverted
        self.big_numbers: list[int] = [] # MIN HEAP, values non inverted
        self.size: int = 0

    def addNum(self, num: int) -> None:
        # Always add to small nums
        heappush(self.small_numbers, -1 * num)

        # then re-balance appropriately
        # A) if the largest small value (first in max heap) is bigger than the smallest big value, move it over
        if len(self.big_numbers) > 0 and -1 * self.small_numbers[0] > self.big_numbers[0]:
            popped = -1 * heappop(self.small_numbers)
            heappush(self.big_numbers, popped)
        
        # B) if the sizes differ by more than 1, shuffle a value
        # if small_numbers is too small, take from big numbers:
        if len(self.small_numbers) < len(self.big_numbers) - 1:
            popped = heappop(self.big_numbers)
            heappush(self.small_numbers, -1 * popped)

        # if big numbers is too small, take from small numbers:
        elif len(self.big_numbers) < len(self.small_numbers) - 1:
            popped = -1 * heappop(self.small_numbers)
            heappush(self.big_numbers, popped)

        # Any time we add a num, these things must be true at the end
        if len(self.big_numbers) > 0:
             assert -1 * self.small_numbers[0] <= self.big_numbers[0]

        assert abs(len(self.small_numbers) - len(self.big_numbers)) <= 1

        self.size += 1
        # print("small: ", self.small_numbers)
        # print("big: ", self.big_numbers)
        

    def findMedian(self) -> float:
        assert abs(len(self.small_numbers) - len(self.big_numbers)) <= 1

        # 1. if even numbers, avg of two tops of heaps
        if self.size % 2 == 0:
            small_top = -1 * self.small_numbers[0]
            big_top = self.big_numbers[0]
            return (small_top + big_top) / 2
        else: # 2. if odd, median is the top of the larger heap [3, 2, 1] [4, 5] == answer is 3
            # 2a
            if len(self.small_numbers) > len(self.big_numbers):
                return -1 * self.small_numbers[0]
            else:
                return self.big_numbers[0]