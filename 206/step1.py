# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node is not None:
            stack.append(node)
            node = node.next

        reversed_head = None
        if stack:
            reversed_head = stack.pop()
        reversed_node = reversed_head

        while stack:
            reversed_node.next = stack.pop()
            reversed_node = reversed_node.next

        if reversed_node is not None:
            reversed_node.next = None

        return reversed_head
