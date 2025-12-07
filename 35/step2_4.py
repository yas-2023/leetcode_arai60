from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        【開区間】 (left, right)
        探索範囲: left_index より大きく、right_index より小さい
        条件: nums[left] < target <= nums[right] を常に維持するイメージ

        ここで、探索範囲がright自身を含まない、right) となっているが、最終的にright_indexがreturnされるため、やや分かりづらい。
        探索範囲 ≠ 解の範囲 という点に注意
        探索中はright_indexが常に現在キープ中の正解であり、探索エリアからは除外されるという考え方(right自身は調べる対象ではなく、すでに分かっている結果だから、探索範囲からは除外する)。
        """
        left_index = -1
        right_index = len(nums)

        # left と right が隣り合うまで続ける（差が1になったら終了）
        while right_index - left_index > 1:
            middle_index = (left_index + right_index) // 2
            middle_value = nums[middle_index]

            if middle_value == target:
                return middle_index

            if middle_value < target:
                # target は mid より大きい -> left を mid に寄せる
                left_index = middle_index
            else:
                # target は mid 以下 -> right を mid に寄せる
                right_index = middle_index

        # 最終的に nums[left] < target <= nums[right] となるため、
        # 挿入位置（target以上の最初の要素）は right_index
        return right_index
