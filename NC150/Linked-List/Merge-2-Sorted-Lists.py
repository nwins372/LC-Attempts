"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]  
Output: [0]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List
def mergeTwoLists_iter(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: #type: ignore
        # create new listnode to represent the start of the merged list
        # another listnode to iterate through the merged list and continue adding

        # while either list is not empty continue to compare the nodes
        # if node1 < node2, mergeNode.next = node1
        # if they're equal then add n1 then n2

        # At the end one of the lists will still have an element so we can just append it

        mergedNode = ListNode()
        headNode = mergedNode
        while list1 and list2:
            if list1.val < list2.val:
                mergedNode.next = list1
                list1 = list1.next
            else:
                mergedNode.next = list2
                list2 = list2.next

            mergedNode = mergedNode.next
        
        if not list1:
             mergedNode.next = list2
        elif not list2:
             mergedNode.next = list1

        return headNode.next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: #type: ignore
        if not list1:
            return list2
        elif not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2