"""
Solution for Moving average from data stream, Time O(1), Space O(1).

Idea:

"""

# Solution
class MovingAverage:
    
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size, self.nums = size, []
    
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.nums.append(val)
        if len(self.nums) > self.size: self.nums.pop(0)
        return sum(self.nums) / len(self.nums)

# Main.
if __name__ == "__main__":
    obj = MovingAverage(3)
    print(obj.next(1), obj.next(10), obj.next(3), obj.next(5))
