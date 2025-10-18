from collections import defaultdict, deque


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        1-pass:
          - counts[ch]: 出現回数
          - candidates: まだ一意かもしれない文字のインデックス（到着順）
          - 文字が重複したタイミングで、先頭から重複済みを削除
        時間: O(n), 空間: O(n)  
        """
        counts = defaultdict(int)
        candidates = deque()

        for i, character in enumerate(s):
            counts[character] += 1
            if counts[character] == 1:
                candidates.append(i)
                continue
            while candidates and counts[s[candidates[0]]] >= 2:
                candidates.popleft()

        if not candidates:
            return -1
        else:
            return candidates[0]
