from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in num_to_index:
                return [num_to_index[need], i]
            num_to_index[num] = i
