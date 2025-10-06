class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        frequency_counts = defaultdict(int)  # デフォルト値は 0
        for number in nums:
            frequency_counts[number] += 1
        top_key = sorted(frequency_counts, key=frequency_counts.get, reverse=True)[:k]
        return top_key
