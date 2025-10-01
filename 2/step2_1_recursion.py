class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def add_digit_recursive(l1, l2, carry):
            if l1 is None and l2 is None and carry == 0:
                return None

            l1_digit = l1.val if l1 is not None else 0
            l2_digit = l2.val if l2 is not None else 0

            total = l1_digit + l2_digit + carry
            node = ListNode(total % 10)
            carry = total // 10

            l1_next = l1.next if l1 is not None else None
            l2_next = l2.next if l2 is not None else None
            higher_digit_node = add_digit_recursive(l1_next, l2_next, carry)
            node.next = higher_digit_node

            return node

        return add_digit_recursive(l1, l2, 0)
