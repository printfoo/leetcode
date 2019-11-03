from __future__ import annotations

# Solution.
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            arr_copy = arr[:]
            for i in range(1, len(arr) - 1):
                if arr[i - 1] > arr[i] < arr[i + 1]:
                    arr_copy[i] = arr[i] + 1
                if arr[i - 1] < arr[i] > arr[i + 1]:
                    arr_copy[i] = arr[i] - 1
            if arr_copy == arr:
                return arr
            arr = arr_copy[:]

# Main.
if __name__ == "__main__":
    arr = [2,1,2,1,1,2,2,1]
    print(Solution().transformArray(arr))
