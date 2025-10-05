from typing import List
import bisect


class KthLargest:
    """Maintain top-k largest numbers in ascending order using bisect."""
    def __init__(self, k: int, nums: List[int]):
        if k <= 0:
            raise ValueError("k must be positive")
        self.k = k
        self.topk_ascending: List[int] = []
        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:
        # 挿入（等しい値は右側）
        bisect.insort_right(self.topk_ascending, val)
        # k超過なら最小（先頭）を落とす
        if len(self.topk_ascending) > self.k:
            self.topk_ascending.pop(0)
        # 返り値：len<k の間は「現時点の最小」を返す
        return self.topk_ascending[0]
