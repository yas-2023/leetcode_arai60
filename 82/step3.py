# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-101, head)
        node = head
        prev_unique_node = dummy_head
        while node is not None:
            while node.next is not None and node.val == node.next.val:
                node = node.next
            if node is prev_unique_node.next:
                prev_unique_node = node
            else:
                prev_unique_node.next = node.next
            node = node.next
        return dummy_head.next
        