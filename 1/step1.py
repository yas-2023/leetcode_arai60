class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_diff = {}
        for value in nums:
            value_to_diff[value] = target - value

        sorted_nums = sorted(nums)
        answer1 = 0
        answer2 = 0
        for index in range(len(nums)):
            if value_to_diff[sorted_nums[index]] in value_to_diff:
                answer1 = sorted_nums[index]
                answer2 = value_to_diff[sorted_nums[index]]
        if answer1 != answer2:
            answer = [nums.index(answer1), nums.index(answer2)]
        else:
            indexes = [i for i, x in enumerate(nums) if x == answer1]
            answer = indexes[:2]
        return answer
