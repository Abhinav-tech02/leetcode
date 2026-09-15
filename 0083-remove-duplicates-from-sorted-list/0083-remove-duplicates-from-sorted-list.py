# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current=head

        while current and current.next: #this loop run till the last node 
            if current.val==current.next.val:
                current.next=current.next.next #checking the duplicate
            
            else:
                current=current.next #if the duplicate condition is not true then current moves forward

        return head

        
        