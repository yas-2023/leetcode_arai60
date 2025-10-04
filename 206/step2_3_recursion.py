# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_from_node(node):
            if node is None or node.next is None:
                return node
            reversed_head = reverse_from_node(node.next)
            node.next.next = node
            node.next = None
            return reversed_head
        return reverse_from_node(head)
