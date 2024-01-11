
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if head==None:
            return None
        dummy_head=Node(0)
        cur=Node(head.val)
        dummy_head.next=cur
        main_point=head.next
        while main_point:
            new_node=Node(main_point.val)
            cur.next=new_node
            cur=cur.next
            main_point=main_point.next 
        
        main_point=head
        cur=dummy_head.next
        while main_point:
            random_point=main_point.random
            if random_point is None:
                cur.random=None
                cur=cur.next
                main_point=main_point.next
            else:
                temp_point=head
                new_temp_point=dummy_head.next
                while temp_point!=random_point:
                    temp_point=temp_point.next
                    new_temp_point=new_temp_point.next
                cur.random=new_temp_point
                cur=cur.next
                main_point=main_point.next
        return dummy_head.next

def build_linked_list(lst):
    # 构建节点
    nodes = [Node(val) for val, _ in lst]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # 设置 random 指针
    for i, (_, random_index) in enumerate(lst):
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0] if nodes else None

input_list = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
head = build_linked_list(input_list)
print(Solution().copyRandomList(head))
