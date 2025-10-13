from typing import List
from itertools import accumulate


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = {0: 1}
        subarray_count = 0

        for prefix_sum in accumulate(nums):
            # 「prefix[j] - prefix[i] = k」を満たす i の個数を足す
            subarray_count += prefix_sum_to_count.get(prefix_sum - k, 0)
            prefix_sum_to_count[prefix_sum] = prefix_sum_to_count.get(prefix_sum, 0) + 1

        return subarray_count
