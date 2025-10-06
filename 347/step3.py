class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter = Counter(nums)
        max_frequency = max(frequency_counter.values())
        buckets = [[] for _ in range(max_frequency + 1)]

        for key, frequency in frequency_counter.items():
            buckets[frequency].append(key)

        top_k = []

        for frequency in range(max_frequency, 0, -1):
            if buckets[frequency]:
                top_k.extend(buckets[frequency])
                if len(top_k) >= k:
                    return top_k[:k]
        return top_k
