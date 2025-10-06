from heapq import heappush, heappop
from typing import List, Tuple


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Grid BFS from (0,0) using a min-heap; push right and down neighbors.
        Uses a visited set to avoid pushing the same cell twice.
        """
        if k <= 0 or not nums1 or not nums2:
            return []

        result: List[Tuple[int, int]] = []
        heap: List[Tuple[int, int, int]] = []  # (sum, row_index, column_index)
        visited: Set[Tuple[int, int]] = set()

        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        while heap and len(result) < k:
            _, row_index, column_index = heappop(heap)
            result.append((nums1[row_index], nums2[column_index]))

            if row_index + 1 < len(nums1) and (row_index + 1, column_index) not in visited:
                heappush(heap, (nums1[row_index + 1] + nums2[column_index], row_index + 1, column_index))
                visited.add((row_index + 1, column_index))
            if column_index + 1 < len(nums2) and (row_index, column_index + 1) not in visited:
                heappush(heap, (nums1[row_index] + nums2[column_index + 1], row_index, column_index + 1))
                visited.add((row_index, column_index + 1))

        return result
