# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_value_from_node(node):
            if node is not None:
                value = node.val
                node = node.next
            else:
                value = 0
            return value, node

        carry = 0
        dummy_head = ListNode(0, None)
        previous_node = dummy_head

        while l1 is not None or l2 is not None:
            # 本当は左辺のl1,l2は返したくないのですが、返さないとインクリメントされないため返しています。何らか工夫の余地がありそうなのですが。
            # step3では関数を使わない書き方に変更しているのですが、関数にする場合でもより洗練された書き方ができないものでしょうか。
            l1_value, l1 = get_value_from_node(l1)
            l2_value, l2 = get_value_from_node(l2)
            total_value = l1_value + l2_value + carry
            carry = total_value // 10
            value = total_value % 10
            node = ListNode(val=value, next=None)
            previous_node.next = node
            previous_node = node

        if carry == 1:
            node = ListNode(val=carry, next=None)
            previous_node.next = node

        return dummy_head.next
