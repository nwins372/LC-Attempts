"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List
from collections import defaultdict
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # type: ignore
    
    # Use the sorted version of each word as a key in a dictionary
    # If the strings are identical after being sorted then they must be anagrams
    word_dict = defaultdict(list)
    for str in strs:
        sorted_str = ''.join(sorted(str))
        word_dict[sorted_str].append(str)
    
    # Return the values for each key (array of string arrays)
    # O(m * nlogn)
    # m = number of strings, n = length of longest string
    return list(word_dict.values())

def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:  # type: ignore
    
    # Represent strings by their character frequencies
    # We are limited to lowercase English letters, so we can make an array of size 26
    # ASCII value of "a" is 97, and "z" is 122


    # eat (e = 101 - 97 = 4), (a = 97 - 97 = 0), (t = 116 - 97 = 19)
    res = defaultdict(list)
    for str in strs:
        char_count = [0] * 26

        for char in str:
            char_count[ord(char) - ord('a')] += 1
        res[tuple(char_count)].append(str)  # keys have to be immutable so we make tuple
    return list(res.values())