from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first_index = 0
        last_index = len(nums) - 1

        while (last_index - first_index) > 1:
            current_index = (first_index + last_index) // 2
            if target >= nums[current_index]:
                first_index = current_index
                continue
            last_index = current_index

        if target == nums[first_index]:
            return first_index
        if target <= nums[last_index]:
            return last_index
        return last_index + 1
