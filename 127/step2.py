from collections import defaultdict, deque
from typing import Deque, List, Set, Tuple


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        1) 前処理: ワイルドカードパターン（'*' で1文字置換）→一致単語群の索引を構築
        2) BFS: beginWord から層を広げ、endWord に到達した段で長さを返す
        """
        # 早期終了: endWord が辞書に無い
        words: Set[str] = set(wordList)
        if endWord not in words:
            return 0

        word_length: int = len(beginWord)
        # beginWord は辞書に無くても探索上は利用する
        words.add(beginWord)

        # パターン -> そのパターンに一致する単語一覧（例: hot -> *ot, h*t, ho*）
        pattern_to_words = defaultdict(set)
        for word in words:
            for i in range(word_length):
                pattern = word[:i] + "*" + word[i + 1 :]
                pattern_to_words[pattern].add(word)

        # BFS 準備
        visited: Set[str] = set([beginWord])
        words_to_visit: Deque[Tuple[str, int]] = deque([(beginWord, 1)])

        # BFS 本体
        while words_to_visit:
            current_word, current_distance = words_to_visit.popleft()

            for i in range(word_length):
                pattern = current_word[:i] + "*" + current_word[i + 1 :]

                neighbors = pattern_to_words.get(pattern)
                if not neighbors:
                    continue

                for next_word in neighbors:
                    if next_word == endWord:
                        return current_distance + 1
                    if next_word not in visited:
                        visited.add(next_word)
                        words_to_visit.append((next_word, current_distance + 1))

        return 0
