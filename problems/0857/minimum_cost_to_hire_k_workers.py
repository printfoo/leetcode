"""
Solution for Minimum Cost to Hire K Workers, Time O(n*logn) Space O(n).

Idea:
There are 2 tricky parts in this problem: 1) Logic and 2) Data Structure.

1) Logic:
Compute r = w/q for each worker i in N and sort r from min to max.
Start by selecting r[:k], now the important observation is that payment P = max(r) * sum(q), where max(r) = r[k].
-- Why? If we satisfy the person who have max(r), others can scale UP to max(r) and they will satisfy.
Now we try the rest r[k+1:N], and repeatedly remove the one with max(q).
-- Why? Remember P = max(r) * sum(q), therefore when max(r) increase, we want to lower sum(q) as much as possible.

2) Data Structure:
In order to implement above logic, we need to maintain 2 list:
r: sorted initially, complexity O(n*logn).
q: sorted in the loop, now if we user sort() every time we encounter a q, the complexity is O(n^2)
However, using a heap (aka, priority queue) can reduce complexity to O(n*logk)
So time complexity is O(n*logn + n*logk) = O(n*logn)

PS: for binary heap, peek (aka. find-min) takes O(1), push (aka. insert) and pop (aka. delete-min) takes O(logk)
"""

# solution
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: "List[int]", wage: "List[int]", K: "int") -> "float":
        r_and_q = sorted((w/q, q) for w, q in zip(wage, quality))
        heap, payment, sum_q = [], float("inf"), 0
        for r, q in r_and_q:
            heapq.heappush(heap, -q)
            sum_q += q
            if len(heap) > K:
                sum_q += heapq.heappop(heap) # -q so +=
            if len(heap) == K: payment = min(payment, r * sum_q)
        return payment

# Main.
if __name__ == "__main__":
    quality = [37,32,14,14,23,31,82,96,81,96,22,17,68,3,88,59,54,23,22,77,61,16,46,22,94,50,29,46,7,33,22,99,31,99,75,67,95,54,31,48,44,96,99,20,51,54,18,85,25,84]
    wage = [453,236,199,359,107,45,150,433,32,192,433,94,113,200,293,31,48,27,15,32,295,97,199,427,90,215,390,412,475,131,122,398,479,142,103,243,86,309,498,210,173,363,449,135,353,397,105,165,165,62]
    K = 20
    print(Solution().mincostToHireWorkers(quality, wage, K))
