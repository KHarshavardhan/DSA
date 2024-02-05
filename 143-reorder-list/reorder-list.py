# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s,f= head,head.next
        while f and f.next:
            s=s.next
            f=f.next.next
        sec=s.next
        p = s.next = None
        while sec:
            temp = sec.next
            sec.next = p
            p = sec
            sec = temp
        first = head
        second = p
        while second:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2

        
