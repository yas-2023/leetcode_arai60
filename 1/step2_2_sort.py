from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # (値, 元インデックス) のタプルリストを作成
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort(key=lambda x: x[0])
        left, right = 0, len(nums_with_index) - 1
        while left < right:
            sum = nums_with_index[left][0] + nums_with_index[right][0]
            if sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif sum < target:
                left += 1
            else:
                right -= 1
