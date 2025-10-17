from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            # 文字列をソート
            key = ''.join(sorted(string))
            groups[key].append(string)
        return list(groups.values())
