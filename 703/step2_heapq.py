from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # k番目の値を先頭に持つヒープ
        self.k = k
        self.topk_ascending = []  # 上位k個を保持するヒープ
        for number in nums:
            self.add(number)

    def add(self, val: int) -> int:
        """上位k個を保つためにvalをヒープに入れ、超過分を落とす。"""
        heapq.heappush(self.topk_ascending, val)
        # kを超えたら最小を捨てる
        if len(self.topk_ascending) > self.k:
            heapq.heappop(self.topk_ascending)
        # ヒープ先頭が常に「k番目に大きい」
        return self.topk_ascending[0]
