from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = {0: 1}

        prefix_sum = 0
        subarray_count = 0
        for num in nums:
            prefix_sum += num
            subarray_count += prefix_sum_to_count.get(prefix_sum - k, 0)
            prefix_sum_to_count[prefix_sum] = prefix_sum_to_count.get(prefix_sum, 0) + 1

        return subarray_count
