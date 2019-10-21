from __future__ import annotations
import heapq

# Solution.
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        heap1 = []
        heap2 = []
        for s1 in slots1:
            heapq.heappush(heap1, s1)
        for s2 in slots2:
            heapq.heappush(heap2, s2)
        while heap1 and heap2:
            s1 = heap1[0]
            s2 = heap2[0]
            if s1[0] > s2[1]:  # 1.start > 2.end
                heapq.heappop(heap2)
            elif s2[0] > s1[1]:  # 2.start > 1.end
                heapq.heappop(heap1)
            elif s1[0] >= s2[0]:  # 1.start >= 2.start
                if s2[1] >= s1[1]:  # 2.end >= 1.end
                    if s1[1] - s1[0] >= duration:
                        return [s1[0], s1[0] + duration]
                    else:
                        heapq.heappop(heap1)
                if s1[1] >= s2[1]:  # 1.end >= 2.end
                    if s2[1] - s1[0] >= duration:
                        return [s1[0], s1[0] + duration]
                    else:
                        heapq.heappop(heap2)
            elif s2[0] >= s1[0]:  # 2.start >= 1.start
                if s1[1] >= s2[1]:  # 1.end >= 2.end
                    if s2[1] - s2[0] >= duration:
                        return [s2[0], s2[0] + duration]
                    else:
                        heapq.heappop(heap2)
                if s2[1] >= s1[1]:  # 2.end >= 1.end
                    if s1[1] - s2[0] >= duration:
                        return [s2[0], s2[0] + duration]
                    else:
                        heapq.heappop(heap1)
                
        return []
        
# Main.
if __name__ == "__main__":
    slots1 = [[10,50],[60,120],[140,210]]
    slots2 = [[0, 5], [0,15],[60,70]]
    duration = 8
    slots1 = [[10,50],[60,120],[140,210]]
    slots2 = [[0,15],[60,70]]
    duration = 12
    print(Solution(). minAvailableDuration(slots1, slots2, duration))
