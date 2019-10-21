from __future__ import annotations

# Solution.
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if len(arr) == 2:
            return (arr[0] + arr[1]) / 2
        diff = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i] + diff == arr[i+1]:
                continue
            elif arr[i] + diff + diff == arr[i+1]:
                return arr[i] + diff
        arr.reverse()
        diff = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i] + diff == arr[i+1]:
                continue
            elif arr[i] + diff + diff == arr[i+1]:
                return arr[i] + diff
        return arr[0]

# Main.
if __name__ == "__main__":
    #arr = [15,13,12]
    #arr = [5,7,11,13]
    arr = [1,1,1,1,1]
    print(Solution().missingNumber(arr))
