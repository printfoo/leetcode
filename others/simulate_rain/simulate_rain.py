"""Simulate rain.
"""

import random

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

if __name__ == "__main__":
    sim = simulateRain()
    while True:
        if sim.rain_drop():
            exit("All wet after {} drops of rain!".format(sim.rain_count))
