# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None
        current=head

        while current:
            temp=current.next #temp stores the next node of current
            current.next=prev  #current node next is pointed to prev
            prev=current        #prev is moved from None to current
            current=temp        #now current pointer is moved to cuRrent.next

        return prev
        