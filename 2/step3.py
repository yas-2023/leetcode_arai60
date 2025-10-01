class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head_node = ListNode()
        tail_node = head_node
        while l1 is not None or l2 is not None or carry == 1:
            l1_digit = l1.val if l1 is not None else 0
            l2_digit = l2.val if l2 is not None else 0
            total = l1_digit + l2_digit + carry
            node = ListNode(total % 10)
            tail_node.next = node

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            carry = total // 10
            node = node.next
            tail_node = tail_node.next
        return head_node.next
