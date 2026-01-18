"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""
from typing import List
def reorderList(self, head: Optional[ListNode]) -> None: #type: ignore
    """
    Do not return anything, modify head in-place instead.
    """
    # Divide the linked list into 2 halves and then reverse the second half to more easily follow the reordered list pattern
    # ex: 1->2->3->4->5 ==> 1->5->2->4->3
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None
    prev = None

    # reverse second half
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # merge until one pointer is null
    first = head
    second = prev #second starts from the end of the second half
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

    
