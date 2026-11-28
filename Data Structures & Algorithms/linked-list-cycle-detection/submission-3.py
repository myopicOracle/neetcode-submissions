# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        curr = head
        while curr:

            if curr in seen:
                return True

            seen.add(curr)
            curr = curr.next

        return False


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         seen = set()

#         curr = head        
#         while curr:

#             seen.add(curr)

#             if curr.next in seen:
#                 return True
            
#             curr = curr.next

#         return False


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
        
#         seen = set()

#         curr = head
#         index = 0

        
#         while curr:

#             if not curr.next:
#                 return False

#             curr.val = index
#             seen.add(index)

#             if curr.next.val in seen:
#                 return True

#             index += 1
#             curr = curr.next

#         return False
