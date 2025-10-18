from typing import List, Set


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        短い方だけ set 化。
        - 時間: O(m + n)
        - 空間: O(min(m, n))
        """
        # 配列の長短を判別して入れ替え（短い方をset化する）
        if len(nums1) > len(nums2):
            short_nums, long_nums = nums2, nums1
        else:
            short_nums, long_nums = nums1, nums2

        candidates: Set[int] = set(short_nums)
        result: Set[int] = set()
        for value in long_nums:
            if value in candidates:
                result.add(value)
        return list(result)
