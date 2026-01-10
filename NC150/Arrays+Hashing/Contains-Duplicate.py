"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

"""
from typing import List
def containsDuplicate(self, nums: List[int]) -> bool:
    # Sort integer array, then loop through the elements and check if the next element is equal to the current element
    # return true if that is the case, return False at the end if condition not met
    # TC: O(nlogn)
    nums.sort()

    for i in range( len(nums) - 1 ):
        if nums[i + 1] == nums[i]:
            return True
    return False

def containsDuplicate2(self, nums: List[int]) -> bool:
    # Create set
    # Elements in set have to be unique so if it already exists in num_set then we know a duplicate exists
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        else:
            num_set.add(num)
    return False

