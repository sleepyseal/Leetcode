# 定义链表节点类
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        while head is not None and head.val==val:
            head=head.next
        p=head
        while p.next:
            if p.next.val==val:
                p.next=p.next.next
            else:
                p=p.next
        return head
def init_linked_list(lst):
    if not lst:  # 空列表情况
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 测试示例
input_list = []
head = init_linked_list(input_list)

s=ListNode()
s.removeElements(head, 6)
current = head
while current:
    print(current.val)
    current = current.next