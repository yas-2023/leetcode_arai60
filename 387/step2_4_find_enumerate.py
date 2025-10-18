class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index, character in enumerate(s):
            if s.find(character, 0, index) == -1 and s.find(character, index+1) == -1:
                return index
        return -1
