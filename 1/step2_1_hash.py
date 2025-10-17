class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index: dict[int, int] = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in num_to_index:
                return [num_to_index[need], i]
            # 補数なしなら今の値を登録
            num_to_index[num] = i
