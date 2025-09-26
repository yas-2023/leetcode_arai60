from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        # 出現回数をカウントする辞書を作成
        freq_dict: dict[int, int] = {}
        while node is not None:
            print(node.val)
            if node.val in freq_dict:
                freq_dict[node.val] += 1
            else:
                freq_dict[node.val] = 1
            node = node.next

        # ユニークな値のみを抽出
        def extract_unique_keys(freq_dict):
            return [key for key, value in freq_dict.items() if value == 1]

        unique_vals = extract_unique_keys(freq_dict)

        # 既存の連結リストからユニークなnodeのみ抽出
        unique_node_list = []
        node = head
        while node is not None:
            if node.val in unique_vals:
                unique_node_list.append(node)
            node = node.next

        # 連結リストのリンクを修正
        for idx, unique_node in enumerate(unique_node_list):
            if idx < len(unique_node_list)-1:
                unique_node.next = unique_node_list[idx+1]
            else:
                unique_node.next = None
        if len(unique_node_list) > 0:
            return unique_node_list[0]
        else:
            return None
