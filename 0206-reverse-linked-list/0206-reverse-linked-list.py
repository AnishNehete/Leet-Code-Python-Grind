# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next #save next_node as first
        
            curr.next = prev  #reversing the link
            prev = curr #move prev one step ahead
            curr = next_node #then move curr one step ahead
        
        return prev