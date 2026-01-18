"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List
def reverseListRecur(self, head: Optional[ListNode]) -> Optional[ListNode]: #type: ignore
    
    if not head:
        return None
    
    dummy = head
    if head.next:
        dummy = self.reverseListRecur(head.next)
        head.next.next = head
    head.next = None
    return dummy

def reverseListIter(self, head: Optional[ListNode]) -> Optional[ListNode]: #type: ignore

    # Intialize 3 pointers - previous node (prev), current node (curr), next node (temp)
    prev = None
    curr = head
    while curr:
        # Store pointer to the next node
        temp = curr.next

        # Set the current node's next pointer to the previous node (reversing)
        curr.next = prev

        # Move the previous pointer forward 
        prev = curr

        # move the current pointer forward
        curr = temp
    
    # prev should be the last element (curr would be null)
    return prev