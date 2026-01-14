"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
from typing import List
def productExceptSelf( nums: List[int]) -> List[int]: #type: ignore
    # brute force
    # create an array to store prefix+suffix excluding the current element
    # iterate through current list but skip that element
    # O(n^2)

    res = [1] * len(nums)
    for i in range( len(nums) ):
        for j in range( len(nums) ):
            if i == j:
                continue
            else:
                res[i] *= nums[j]
    return res

def productExceptSelf2( nums: List[int]) -> List[int]: #type: ignore
    # Using prefix + suffix array
    # for each element store the prefix products in the prefix List and the suffix in the suffix List
    n = len(nums)
    res = [1] * n
    
    prefix, suffix = 1, 1

    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    for i in range( n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res

def main():
    print("hello")
    nums_test = [1,2,3,4]
    print( productExceptSelf2(nums_test) )

if __name__ == "__main__":
    main()