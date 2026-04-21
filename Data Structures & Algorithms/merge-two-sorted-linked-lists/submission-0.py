# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next=list2

        return dummy.next
        
        
        
        
        
        # curr1 = head1
        # curr2= head2
        
        # if curr1.val > curr2.val:
        #     curr1 = head1
        #     curr1 = curr2.next
        # else:
        #     curr2=head1

        # return curr1
        