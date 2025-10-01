from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        # 連結リストの最後の要素または None の場合は、そのまま返す
        if (node is None) or (node.next is None):
            return node

        # 再帰的にリンクをつなぎ直す
        node.next = self.deleteDuplicates(node.next)
        # 隣が同値なら、自分をスキップして node.next を返す
        return node.next if node.val == node.next.val else node
