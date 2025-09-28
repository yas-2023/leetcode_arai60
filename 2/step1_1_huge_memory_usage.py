# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_int(node):
            output_number = 0
            base_number = 0
            while node is not None:
                output_number += node.val * 10 ** base_number
                base_number += 1
                node = node.next
            return output_number

        def int_to_list(input_number):
            output_list_number = []
            while input_number >= 0:
                output_list_number.append(ListNode(input_number % 10, None))
                input_number //= 10
            if len(output_list_number) > 1:
                for index in range(len(output_list_number) - 1):
                    print(index)
                    output_list_number[index].next = output_list_number[index+1]

            return output_list_number[0]

        total_value = list_to_int(l1) + list_to_int(l2)
        return int_to_list(total_value)
        