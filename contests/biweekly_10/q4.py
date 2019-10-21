# Solution.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        residue_dict = {}
        for i in range(len(nums)):
            try:
                return [residue_dict[nums[i]], i]
            except KeyError:
                residue_dict[target - nums[i]] = i

# Main.
if __name__ == "__main__":
    nums = [1, 2, 4, 5, 6]
    target = 5
    solution = Solution()
    print(Solution().twoSum(nums, target))
