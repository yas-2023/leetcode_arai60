class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index, character in enumerate(s):
            # findとrfindでその文字が最初に現れるインデックスと最後に現れるインデックスが同じなら、一意
            if s.find(character) == s.rfind(character):
                return index
        return -1
