# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy_head=ListNode(0)
        dummy_head.next=head
        cur= head
        pre= dummy_head
        i=1
        while i<right:
            if i <left:
                pre=cur
                cur=cur.next 
                i=i+1
            elif i>=left and i <right:
                temp=cur.next
                if temp is not None:
                    temp2=pre.next
                    pre.next=temp
                    cur.next=temp.next 
                    temp.next=temp2
                else:
                    pass
                i=i+1
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
input_list = [3,5]
head = init_linked_list(input_list)
s=Solution()
current=s.reverseBetween(head,1,2)
while current:
    print(current.val)
    current = current.next