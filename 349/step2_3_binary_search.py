from bisect import bisect_left
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        二分探索法
        短い配列の値が長い配列に存在するかを二分探索する。
        - m = len(short_nums)
        - n = len(long_nums)
        - 時間: O(m log n)（ソート込みで O(m log m + n log n + m log n)）
        - 空間: O(1)
        """
        # 配列の長短を判別
        if len(nums1) <= len(nums2):
            short_nums, long_nums = nums1, nums2
        else:
            short_nums, long_nums = nums2, nums1

        short_nums.sort()
        long_nums.sort()

        def exists_in_long(x: int) -> bool:
            """long_nums に x が存在するか（二分探索）"""
            idx = bisect_left(long_nums, x)
            return idx < len(long_nums) and long_nums[idx] == x

        result: List[int] = []
        i = 0
        last_pushed = None

        # 短い配列側の重複をまとめてスキップしつつ、各値を一度だけ探索
        while i < len(short_nums):
            short_value = short_nums[i]
            if exists_in_long(short_value) and last_pushed != short_value:
                result.append(short_value)
                last_pushed = short_value
            # 同じ値をスキップ
            while i < len(short_nums) and short_nums[i] == short_value:
                i += 1

        return result
