"""
Solution for Heaters, Time O(m*logm + n*logn).

Idea:
For each house, find its left-closest and right-closest heaters and get min dist, finally find max of dist list.
Keep moving pointers for heaters to avoid duplicated comparison.
"""

# Solution.
class Solution:
    def findRadius(self, houses: "List[int]", heaters: "List[int]") -> "int":
        houses.sort()
        heaters.sort()
        heaters = [-float("inf")] + heaters + [float("inf")]
        dist, heater_i = [], 0
        for house in houses:
            while heaters[heater_i] < house: heater_i += 1
            dist.append(min(house - heaters[heater_i - 1], heaters[heater_i] - house))
        return max(dist)

# Main.
if __name__ == "__main__":
    houses = [1,5]
    heaters = [10]
    print(Solution().findRadius(houses, heaters))
