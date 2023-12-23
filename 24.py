# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head= ListNode(0)
        dummy_head.next=head
        pre=dummy_head
        cur=head 
        while cur is not None and cur.next is not None:
            next_node=cur.next 
            tail_node=next_node.next 
            pre.next=next_node
            next_node.next=cur 
            cur.next=tail_node 

            pre=cur
            cur=pre.next 
        return dummy_head.next 

def init_linked_list(lst):
    if lst is None:
        return None
    
    head=ListNode(lst[0])
    cur=head
    for i in lst[1:]:
        cur.next=ListNode(i)
        cur=cur.next
    return head   

input_list = [1]
head = init_linked_list(input_list)

s=Solution()
head= s.swapPairs(head)
current = head
while current:
    print(current.val)
    current = current.next