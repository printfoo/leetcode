# Remove.

from __future__ import annotations

# Solution.
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        max_sum_div_3 = sum(nums)
        if max_sum_div_3 % 3 == 0:
            return max_sum_div_3
        left_1 = [n for n in nums if n % 3 == 1]
        left_2 = [n for n in nums if n % 3 == 2]
        left_1.sort()
        left_2.sort()
        if max_sum_div_3 % 3 == 1:
            if_remove_two_left_2 = left_2[0] + left_2[1] if len(left_2) > 1 else float("inf")
            if_remove_one_left_1 = left_1[0] if len(left_1) > 0 else float("inf")
            if if_remove_two_left_2 < if_remove_one_left_1:
                max_sum_div_3 -= if_remove_two_left_2
            else:
                max_sum_div_3 -= if_remove_one_left_1
            return max_sum_div_3
        if max_sum_div_3 % 3 == 2:
            if_remove_two_left_1 = left_1[0] + left_1[1] if len(left_1) > 1 else float("inf")
            if_remove_one_left_2 = left_2[0] if len(left_2) > 0 else float("inf")
            if if_remove_two_left_1 < if_remove_one_left_2:
                max_sum_div_3 -= if_remove_two_left_1
            else:
                max_sum_div_3 -= if_remove_one_left_2
            return max_sum_div_3

# Main.
if __name__ == "__main__":
    nums = [366,809,6,792,822,181,210,588,344,618,341,410,121,864,191,749,637,169,123,472,358,908,235,914,322,946,738,754,908,272,267,326,587,267,803,281,586,707,94,627,724,469,568,57,103,984,787,552,14,545,866,494,263,157,479,823,835,100,495,773,729,921,348,871,91,386,183,979,716,806,639,290,612,322,289,910,484,300,195,546,499,213,8,623,490,473,603,721,793,418,551,331,598,670,960,483,154,317,834,352]
    print(Solution().maxSumDivThree(nums))
