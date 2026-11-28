# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # find index of current node
        # ... if index matches n,connect prev to next 

        index, length = 0, 0
        dummy = ListNode(0, head)

        curr = head
        while curr:
            length += 1
            curr = curr.next

        # print("length:", length)
        pos = length - n

        curr = head
        prev = dummy
        while curr:

            if index == pos:
                prev.next = curr.next
                break

            index += 1
            prev = curr
            curr = curr.next 

        return dummy.next
