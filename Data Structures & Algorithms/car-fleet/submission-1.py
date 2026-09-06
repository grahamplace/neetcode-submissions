from _heapq import heappop
'''
n cars 
position arr (n) - position of each car in miles
speed arr (n) - speed of each car in mph

destination is at position `target` miles

cars cannot pass, if they catch a car they then take on that cars speed
car fleet is 1+ cars at the same pos and same speed

so basically cars catch up to next car, join fleet, etc

they reach the end together

'''

from heapq import heappush, heappop

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return -1

        h = []
        for i in range(len(position)):
            i_pos = position[i]
            i_speed = speed[i]
            i_distance_to_cover = (target - i_pos)
            i_time_to_dest = i_distance_to_cover / i_speed
            heappush(h, (i_distance_to_cover, i_time_to_dest, i))
        
        fleet_time = 0
        fleets = 0
        while h:
            _, car_time, _ = heappop(h)
            # if this car arrives later than the fleet ahead of it, then it doesn't join that fleet
            if car_time > fleet_time:
                fleets += 1
                fleet_time = car_time

        return fleets