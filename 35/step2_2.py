from typing import List

# 閉区間
"""
    【閉区間】 [left, right]
    探索範囲: left_index 以上、right_index 以下
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1

        while first <= last:
            middle = (first + last) // 2
            # 分岐が増えパフォーマンスは低下するように思われるが理解はしやすい
            if target == nums[middle]:
                return middle
            if target > nums[middle]:
                first = middle + 1
            else:
                last = middle - 1

        return first
