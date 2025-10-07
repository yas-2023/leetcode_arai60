from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            char_counter = Counter(string)
            groups[frozenset(char_counter.items())].append(string)
        return list(groups.values())
