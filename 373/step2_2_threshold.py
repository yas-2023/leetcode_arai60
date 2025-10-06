from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        しきい値（sum <= T）を二分探索で求めて一括回収
        - まず、a+b <= T となるペア数が k 以上になる最小 T を二分探索で見つける
        - 次に、sum < T のペアを全件回収し、足りない分を sum == T から補充
        return順は不問, 必要なら最後に和でソート可能。
        """

        nums1_length, nums2_length = len(nums1), len(nums2)

        # a+b <= threshold のペア数を O(m+n) で数える（2ポインタ）
        def count_pairs_leq(threshold: int) -> int:
            count = 0
            j = nums2_length - 1  # nums2 の右端から左へ
            for i in range(nums1_length):
                a = nums1[i]
                while j >= 0 and a + nums2[j] > threshold:
                    j -= 1
                if j < 0:
                    break
                count += (j + 1)
            return count

        # しきい値 T* を二分探索
        low = nums1[0] + nums2[0]
        high = nums1[nums1_length-1] + nums2[nums2_length-1]
        while low < high:
            mid = (low + high) // 2
            if count_pairs_leq(mid) >= k:
                high = mid
            else:
                low = mid + 1
        threshold = low

        result: List[List[int]] = []

        # sum < threshold を行単位で一括回収
        for i in range(nums1_length):
            a = nums1[i]
            # a + b < threshold  <=>  b < threshold - a
            j_end = bisect_left(nums2, threshold - a)
            # nums2[0:j_end] が条件を満たす
            for j in range(j_end):
                result.append([a, nums2[j]])
                if len(result) == k:
                    return result

        # 不足分を sum == threshold から補充
        if len(result) < k:
            for i in range(nums1_length):
                a = nums1[i]
                need = threshold - a
                left = bisect_left(nums2, need)
                right = bisect_right(nums2, need)
                for j in range(left, right):
                    result.append([a, nums2[j]])
                    if len(result) == k:
                        return result
