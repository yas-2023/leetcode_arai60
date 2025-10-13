from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = defaultdict(int)
        prefix_sum_to_count[0] = 1

        curr_sum = 0
        subarray_count = 0
        for value in nums:
            curr_sum += value
            subarray_count += prefix_sum_to_count[curr_sum - k]
            prefix_sum_to_count[curr_sum] += 1

        return subarray_count
