from heapq import heappush, heappop
from typing import List, Tuple


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        k_smallest_pairs: List[Tuple[int, int]] = []
        heap: List[Tuple[int, int, int]] = []  # (sum, row_index, col_index)

        max_rows = min(k, len(nums1))
        for row_index in range(max_rows):
            heappush(heap, (nums1[row_index] + nums2[0], row_index, 0))

        while heap and len(k_smallest_pairs) < k:
            _, row_index, column_index = heappop(heap)
            k_smallest_pairs.append((nums1[row_index], nums2[column_index]))
            if column_index + 1 < len(nums2):
                heappush(heap, (nums1[row_index] + nums2[column_index + 1], row_index, column_index + 1))

        return k_smallest_pairs
