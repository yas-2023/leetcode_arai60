class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        def get_cumsum(nums, k):
            cumsum = []
            sum_ = 0
            for num in nums:
                sum_ = sum_ + num
                cumsum.append(sum_)
            return cumsum

        result = 0
        for i in range(len(nums)):
            cumsum = get_cumsum(nums[i:], k)
            result = result + cumsum.count(k)
        return result
