"""
Clever solution for Two Sum, O(n).

Idea:
Use a residue_dict, each key-value pair subject to: key + nums[value] == target,
i.e., {residue if choose nums[j]: j}
Iterate over indexes of nums i:
If nums[i] in the residue dict,
    we know by choosing j, the residue is exactly nums[j] == nums[i], therefore we choose [i, j];
Otherwise,
    we record the residue when choosing i.
"""

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
    print(solution.twoSum(nums, target))
