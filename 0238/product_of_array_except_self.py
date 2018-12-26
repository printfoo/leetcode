"""
Solution for product of array except self, Time O(n), Space O(1) (except output).

Idea:
Traverse twice, from head to tail and tail to head, e.g.,
nums:   [   1,   2,   3,    4   ]
1st:    [   -,   1,  12,  123   ]
2nd:    [ 234, 134, 124,  123   ]
"""

# Solution.
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output, len_nums = [], len(nums)
        # first traverse
        prod = 1
        for i in range(len_nums):
            output.append(prod)
            prod *= nums[i]
        # second traverse
        prod = 1
        for i in range(len_nums - 1, -1, -1):
            output[i] *= prod
            prod *= nums[i]
        return output

# Main.
if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))
