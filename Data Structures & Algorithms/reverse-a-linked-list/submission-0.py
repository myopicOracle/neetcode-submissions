# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        vals = []

        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        # print(vals)
        vals.reverse()
        # print(vals)

        def createLinkedList(values):
            dummy = ListNode()  
            curr = dummy        
            
            for val in values:
                curr.next = ListNode(val)
                curr = curr.next

            return dummy.next


        return createLinkedList(vals)



