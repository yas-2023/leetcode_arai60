from typing import Dict, Tuple


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count_first_index: Dict[str, Tuple[int, int]] = {}  # (count, first_index)
        # 1周目: (回数, 最初のindex) を構築
        for index, character in enumerate(s):
            if character in char_to_count_first_index:
                count, first_index = char_to_count_first_index[character]
                char_to_count_first_index[character] = (count + 1, first_index)
            else:
                char_to_count_first_index[character] = (1, index)

        # 2周目: 回数==1 の first_index 最小を探索
        min_index = float("inf")
        for count, first_index in char_to_count_first_index.values():
            if count == 1 and first_index < min_index:
                min_index = first_index

        if min_index == float("inf"):
            min_index = -1

        return min_index
