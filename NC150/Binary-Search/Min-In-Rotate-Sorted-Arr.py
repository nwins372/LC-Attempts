"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 

For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 
1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
from typing import List
def findMin2(nums: List[int]) -> int: #type: ignore
    # Brute Force would be to iterate through the array and find the min, but that's O(n)
    l = 0
    r = len(nums) - 1
    minVal = nums[0]

    while l <= r:
        # if left pointer is less than right pointer we assume the array is already sorted
        if nums[l] < nums[r]:
            minVal = min(minVal, nums[l])
            break
        mid = (l + r) // 2
        minVal = min(minVal, nums[mid])
        # if mid > left pointer, we know that the pivot is somewhere to the right
        if nums[mid] >= nums[l]:
            l = mid+1
        # else if mid > right 
        else:
            r = mid-1
        
    return minVal

def findMin(nums: List[int]) -> int: #type: ignore
    # Brute Force would be to iterate through the array and find the min, but that's O(n)
    l = 0
    r = len(nums) - 1
    minVal = nums[0]

    while l < r:
        mid = (l + r) // 2
        minVal = min(minVal, nums[mid])
        # if middle value greater than the right pointer, ex [3,4,5,1,2]
        # the pivot must be somewhere to the right of mid
        if nums[mid] > nums[r]:
            l = mid + 1
        # else if mid < right, ex [8,9,1,2,3,4,5,6,7]
        # the numbers keep increasing to the right, so we should look to the left
        else:
            r = mid
    return nums[l]
def main():
    nums = [4,5,6,7,0,1,2]
    print(f"Initial arr {nums}")
    print( f"Min Value = {findMin(nums)}" )

if __name__ == "__main__":
    main()