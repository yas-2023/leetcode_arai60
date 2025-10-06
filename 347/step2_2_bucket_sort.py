# 解法2: Bucket Sort（理論上の最速 O(n)）
# 時間計算量: O(n) / 空間: O(n)  ※bucketの長さは n+1
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter = Counter(nums)
        max_frequency = max(frequency_counter.values())
        # index = 出現回数
        # 値 = その回数の要素リスト
        buckets: List[List[int]] = [[] for _ in range(max_frequency + 1)]
        for key, frequency in frequency_counter.items():
            buckets[frequency].append(key)

        top_k: List[int] = []
        # 高頻度から取り出す
        for frequency in range(max_frequency, 0, -1):
            if buckets[frequency]:
                top_k.extend(buckets[frequency])
                if len(top_k) >= k:
                    return top_k[:k]
        return top_k  # len(top_k) < k
