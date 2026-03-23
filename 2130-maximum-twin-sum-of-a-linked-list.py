#Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast , slow = head, head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        max_sum = 0
        first ,second = head, prev
        while second:
            max_sum =  max(max_sum,first.val+second.val)
            first = first.next
            second = second.next
        return max_sum

# tests
# Input: head = [5,4,2,1]
# Output: 6
#run 
sol = Solution()
head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
print(sol.pairSum(head))  # Expected output: 6