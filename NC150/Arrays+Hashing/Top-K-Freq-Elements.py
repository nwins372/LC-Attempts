"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:  # type: ignore
    # Get frequency of each number and store it in dictionary
    # Make pairs of [number, frequency]
    num_freq = {}
    freq_arr = [[] for i in range(len(nums) + 1)]

    for num in nums:
        num_freq[num] = 1 + num_freq.get(num, 0)

    # Stores number and their frequency
    # numbers that appear 2x will be in freq_arr[2]
    for num, frq in num_freq.items():
        freq_arr[frq].append(num)

    res = []
    # Add each number of the corresponding element frequency until k is reach
    for i in range( len(freq_arr) -1, 0, -1 ):
        for num in freq_arr[i]:
            res.append(num)
        if len(res) == k: return res

def main():
     nums = [1,1,1,2,2,3]
     k = 2
     print("test")
     print( topKFrequent(nums, k) )
    
if __name__ == '__main__':
    main()