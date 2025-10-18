class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index, character in enumerate(s):
            if s.index(character) == s.rindex(character):
                return index
        return -1
