"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List
def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
    # Brute Force (O(n^2))
    # For each element, see if there is another element that adds up to the target value

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
def twoSum2(self, nums: List[int], target: int) -> List[int]: # type: ignore
    # Create a dictionary to store previously seen values
    # As we iterate through nums, we check if a previously seen value added with the current value sums up to target
    # O(n) time complexity

    num_dict = {}

    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in num_dict:
            return [i, num_dict[compliment]]
        else:
            num_dict[nums[i]] = i
                   