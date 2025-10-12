from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        2ポインタ解法
        - 時間:
            既にソート済みなら O(m + n)、
            ソートを含めると O(m log m + n log n)。
        - 空間: O(1)
        """
        # ソート
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        result: List[int] = []
        last_pushed = None  # 同じ要素を重複して追加しないため

        while i < len(nums1) and j < len(nums2):
            nums1_value, nums2_value = nums1[i], nums2[j]
            if nums1_value == nums2_value:
                if last_pushed != nums1_value:
                    result.append(nums1_value)
                    last_pushed = nums1_value
                # 同じ値をスキップ
                while i < len(nums1) and nums1[i] == nums1_value:
                    i += 1
                while j < len(nums2) and nums2[j] == nums2_value:
                    j += 1
            elif nums1_value < nums2_value:
                while i < len(nums1) and nums1[i] == nums1_value:
                    i += 1
            else:
                while j < len(nums2) and nums2[j] == nums2_value:
                    j += 1

        return result
