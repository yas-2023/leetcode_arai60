# 解法3: Quickselect（平均 O(n)）
# 配列を（頻度で）k番目以降が右側に来るよう分割し、右側 k 個を返す
# 平均的には全部を順番に並べる必要はないので早い
# 時間計算量: 平均 O(m) / 空間: O(m)（Counter分）
from collections import Counter
from typing import List
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter = Counter(nums)
        unique_values = list(frequency_counter.keys())

        def swap(list_object, index_a, index_b):
            list_object[index_a], list_object[index_b] = list_object[index_b], list_object[index_a]

        def partition(left, right, pivot_index):
            pivot_frequency = frequency_counter[unique_values[pivot_index]]
            # pivot を右端とswap(比較処理中に pivot が邪魔にならないように、一時的に末尾へ移動。)
            swap(unique_values, right, pivot_index)
            lower_frequency_store_index = left
            # 低頻度を左へ
            for index in range(left, right):
                if frequency_counter[unique_values[index]] < pivot_frequency:
                    swap(unique_values, lower_frequency_store_index, index)
                    lower_frequency_store_index += 1
            # rightに保存していたpivot_indexを確定位置に戻す
            swap(unique_values, lower_frequency_store_index, right)
            return lower_frequency_store_index

        def select_k_largest_by_frequency(k_smallest_from_end):
            left = 0
            right = len(unique_values) - 1
            target_index = len(unique_values) - k_smallest_from_end # 左から数えたindexに変換
            while True:
                pivot_index = random.randint(left, right)
                pivot_index = partition(left, right, pivot_index)
                if pivot_index == target_index:
                    return
                elif pivot_index < target_index:
                    left = pivot_index + 1
                else:
                    right = pivot_index - 1

        select_k_largest_by_frequency(k)
        return unique_values[-k:]
