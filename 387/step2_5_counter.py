from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for index, character in enumerate(s):
            if counts[character] == 1:
                return index
        return -1
