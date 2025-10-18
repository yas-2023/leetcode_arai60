from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count = Counter(s)
        for index, character in enumerate(s):
            if char_to_count[character] == 1:
                return index
        return -1
