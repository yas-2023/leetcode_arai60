# stack解法
# 方針：
# 1.現在の値が前後の値と違うならpushしていく
# 2.最後にリンクを修正する

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 前後の値を比較する方針上、最初のノードを処理する際に、そのノードより前のダミーヘッドを作成
        # 与えられるvalは-100以上という制約があるのでdummy_headの値には-101を指定
        dummy_head = ListNode(val=-101, next=head)

        curr_node = head
        prev_node = dummy_head

        stack = []
        while curr_node is not None:

            # 最終ノードではない場合
            if (curr_node.next is not None) and (curr_node.val != prev_node.val) and (curr_node.val != curr_node.next.val):
                stack.append(curr_node)
                # print(prev_node.val,curr_node.val,curr_node.next.val)
            # 最終ノードの場合
            elif (curr_node.next is None) and (curr_node.val != prev_node.val):
                stack.append(curr_node)
                # print(prev_node.val,curr_node.val)

            prev_node = curr_node
            curr_node = curr_node.next

        # 連結リストのリンクを修正
        for idx, unique_val_node in enumerate(stack):
            if idx < len(stack)-1:
                unique_val_node.next = stack[idx+1]
            else:
                unique_val_node.next = None
        if len(stack) > 0:
            return stack[0]
        else:
            return None
