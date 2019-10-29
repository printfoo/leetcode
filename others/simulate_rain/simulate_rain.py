"""
Solution for Simulate Rain.

Idea:
Way representation: 100 slots, each 1 centimeter.
Rain representation: center point random [0, 1], and +- 0.5 for area.
"""

import random
import numpy as np

class simulateRain:
    def __init__(self):
        self.way = [[i, i + 1] for i in range(100)]
        self.wet_centimeter = 0
        self.rain_count = 0
    
    def rain_drop(self):
    
        # Randomly rains.
        self.rain_count += 1
        rain = random.random() * 100  # Center of the rain drop.
        left = rain - 0.5 if rain > 0.5 else None  # Wet area of the left slot.
        right = rain + 0.5 if rain < 99.5 else None  # Wet area of the right slot.
        
        # Updates left slot.
        if left and self.way[int(left)][0] < self.way[int(left)][1]:  # If left slot is not already wet.
            self.way[int(left)][1] = min(left, self.way[int(left)][1])  # Update right side of the left slot.
            if self.way[int(left)][0] >= self.way[int(left)][1]:  # If it is wet now.
                self.wet_centimeter += 1  # Count wet.
        
        # Updates right slot.
        if right and self.way[int(right)][0] < self.way[int(right)][1]:  # If right slot is not already wet.
            self.way[int(right)][0] = max(right, self.way[int(right)][0])  # Update left side of the right slot.
            if self.way[int(right)][0] >= self.way[int(right)][1]:  # If it is wet now.
                self.wet_centimeter += 1  # Count wet.

        return True if self.wet_centimeter == 100 else False  # All wet or not.

def simulate_once():
    sim = simulateRain()
    while True:
        if sim.rain_drop():
            return sim.rain_count
            
if __name__ == "__main__":
    exp = 1000
    rain_counts = [simulate_once() for _ in range(exp)]
    mean = np.mean(rain_counts)
    std = np.std(rain_counts)
    print("Simulated {} times of rain drops: mean {:.2f}, std {:.2f}.".format(exp, mean, std))
