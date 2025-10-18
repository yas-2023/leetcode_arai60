class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        while nums and k < len(nums):
            nums.remove(min(nums))
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
        elif val > min(self.nums):
            self.nums.remove(min(self.nums))
            self.nums.append(val)
        return min(self.nums)
