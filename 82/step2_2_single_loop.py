# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-101, head)
        node = head
        prev_node = dummy_head
        val_to_remove = None

        while node is not None:
            # 同値が続く場合はノードを右に動かし続ける
            if node.val == val_to_remove:
                # print("continuous",node.val)
                node = node.next
                continue
            # 同値の場合(初回のみ)
            if node.next is not None and node.val == node.next.val:
                # print("continuous2",node.val)
                val_to_remove = node.val
                prev_node.next = None
                node = node.next
                continue
            # 同値ではない場合
            # print("not continuous",node.val)
            prev_node.next = node
            prev_node = node
            node = node.next
        return dummy_head.next
