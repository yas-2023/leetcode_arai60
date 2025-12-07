from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        【半開区間】 [left, right)
        探索範囲: left_index 以上、right_index 未満
        """
        left_index = 0
        right_index = len(nums)  # 配列の長さ（インデックスとしては範囲外）

        # left と right が重なったら終了（範囲が空）
        while left_index < right_index:
            middle_index = (left_index + right_index) // 2
            middle_value = nums[middle_index]

            if middle_value == target:
                return middle_index

            if middle_value < target:
                # mid は探索済みなので、左端を mid の右へ
                left_index = middle_index + 1
            else:
                # mid はターゲットより大きい
                # right は「範囲に含まない」定義なので、そのまま mid を代入
                right_index = middle_index

        # 終了時は left_index == right_index となる
        return left_index
