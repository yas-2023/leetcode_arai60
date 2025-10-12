from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            long_nums = nums1
            short_nums = nums2
        else:
            long_nums = nums2
            short_nums = nums1

        candidates = set(short_nums)
        results = set()

        for value in long_nums:
            if value in candidates:
                results.add(value)

        return list(results)
