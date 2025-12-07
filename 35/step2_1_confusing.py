from typing import List


# 閉区間
# 動作することは理解できるが、直感的な理解が難しかった参考コード
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            # if arr[mid] >= target: targetが主役のほうが個人的にはわかりやすいので修正した
            if target <= nums[middle]:
                right = middle - 1
                # nums[middle]がtargetだった場合でもmiddle - 1(middleが探索範囲外になる)になることに違和感
                # -1しないと無限ループになるケースがあることは理解できるが。
                # nums[middle]がtargetだった場合、次ループ以降で+1されるので、最終的な結果は問題ないのだが
                # 私には直感的な理解が難しく感じました。
                # 複数の方がこのように書いておられたので、自然な解釈も存在するのかもしれない
                # 無理やり解釈するなら、middleは最後に確認するので、ひとまずmiddle-1の範囲を先に確認するという理解か
            else:
                left = middle + 1
        return left
