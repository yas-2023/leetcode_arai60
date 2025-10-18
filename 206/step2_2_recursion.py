# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_remaining_node(rest_head, reversed_head):
            if rest_head is None:
                return reversed_head

            latest_rest_head = rest_head.next
            latest_reversed_head = rest_head
            latest_reversed_head.next = reversed_head
            return reverse_remaining_node(latest_rest_head, latest_reversed_head)
        return reverse_remaining_node(head, None)
