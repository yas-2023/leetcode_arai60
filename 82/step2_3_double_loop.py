# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 最初のノードが重複していて消える可能性があるのでダミーヘッドを作成
        # 与えられるvalは-100以上という制約があるのでdummy_headの値には-101を指定
        dummy_head = ListNode(val=-101, next=head)

        curr_node = head
        # prev_unique_nodeは重複のない直前のノードを示す
        prev_unique_node = dummy_head
        while curr_node is not None:
            # 同値が連続する間、ノードを右に動かし続ける
            while (curr_node.next is not None) and (curr_node.val == curr_node.next.val):
                # print(curr_node.val)
                curr_node = curr_node.next
            # 同値が連続せず値がユニークな場合、次回のループのために現在のノードをprev_unique_nodeとする
            if prev_unique_node.next is curr_node:
                # print("unique:", curr_node.val)
                # 値がユニークなので、prev_unique_nodeを更新する
                prev_unique_node = curr_node
            # 同値が連続していた場合はリンクを修正する
            else:
                # prev_unique_node.next は同値が連続しない前提の仮置きのため、同値連続時は修正が必要
                prev_unique_node.next = curr_node.next
                # 同値連続なのでprev_unique_nodeの更新は不要
            curr_node = curr_node.next
        return dummy_head.next

