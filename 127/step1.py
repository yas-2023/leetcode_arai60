from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def find_adjacency_words(target_word, wordList):
            adjacency_words = []
            for word in wordList:
                different_character_counter = 0
                for i in range(len(target_word)):
                    if target_word[i] != word[i]:
                        different_character_counter += 1
                    if different_character_counter >= 2:
                        break
                if different_character_counter == 1:
                    adjacency_words.append(word)
            return adjacency_words

        def find_candidate_words(previous_candidate_words):
            candidate_words = set()
            for previous_word in previous_candidate_words:
                candidate_words.update(adjacency[previous_word])
            return candidate_words

        if endWord not in wordList:
            return 0

        adjacency = defaultdict(list)
        adjacency[beginWord] = find_adjacency_words(beginWord, wordList)
        for word in wordList:
            adjacency[word] = find_adjacency_words(word, wordList)

        previous_words = set([beginWord])
        for number_of_words in range(2, len(wordList) + 2):
            candidate_words = find_candidate_words(previous_words)
            if endWord in candidate_words:
                return number_of_words
            previous_words = candidate_words
        return 0
