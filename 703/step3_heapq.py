from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.topk_ascending = []
        for number in nums:
            self.add(number)

    def add(self, val: int) -> int:
        heapq.heappush(self.topk_ascending, val)
        if len(self.topk_ascending) > self.k:
            heapq.heappop(self.topk_ascending)
        return self.topk_ascending[0]
