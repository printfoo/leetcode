"""
Solution for Flattern 2D Vector.

Idea:

"""

# Solution.
class Vector2D(object):
    
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d, self.i, self.j = vec2d, -1, 0
    
    def next(self):
        """
        :rtype: int
        """
        if self.i + 1 < len(self.vec2d[self.j]): self.i += 1 # same row
        else:
            while not self.vec2d[self.j + 1]: self.j += 1
            self.i = 0; self.j += 1 # next row
        return self.vec2d[self.j][self.i]
    
    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.vec2d: return False # vec2d = []
        if self.i + 1 < len(self.vec2d[self.j]): return True # same row
        temp_j = self.j
        while temp_j + 1 < len(self.vec2d) and not self.vec2d[temp_j + 1]: temp_j += 1
        if temp_j + 1 < len(self.vec2d): return True # next row
        return False

# Main.
if __name__ == "__main__":
    vec2d = [[], [1,2], [], [3], []]
    i, v = Vector2D(vec2d), []
    while i.hasNext(): v.append(i.next())
    print(v)
