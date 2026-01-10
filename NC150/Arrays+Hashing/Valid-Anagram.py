"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

def isAnagram(self, s: str, t: str) -> bool:
    # nlogn + mlogm
    return sorted(s) == sorted(t)

def isAnagram2(self, s: str, t: str) -> bool:

    # If lengths aren't the same they can't be anagrams
    if len(s) != len(t): return False
    
    countA = {}
    countB = {}

    # If they are anagrams, the frequency of each letter should be the same
    for i in range( len(s)) :
        countA[ s[i] ] = countA.get( s[i], 0) + 1
        countB[ t[i] ] = countB.get( t[i], 0) + 1       

    return countA == countB