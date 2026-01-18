"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?
"""
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: #type: ignore
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # dummy starts just before the head of the list 
    # we leave a distance of n between the left and right pointers
    # we then loop until right reaches the end of the list
    # to remove the nth element from the end we need to access the element right before it
    # so we can set that element's .next to the element after the nth from end element
    # because dummy is before the head of the list we have a gap of n+1 from the end (so we can access the before element)

    # alternate solution, one loop to find out how many elements are in the list
    # the index to remove is Num of Elements - n
    # another loop to iterate up until that index and then remove the element (cur.next = cur.next.next)
    counter = 0
    while counter < n and right:
        right = right.next
        counter += 1

    while right:
        left = left.next # type: ignore
        right = right.next

    left.next = left.next.next # type: ignore

    return dummy.next