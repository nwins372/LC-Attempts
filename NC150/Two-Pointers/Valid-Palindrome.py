"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        # 1. Move Left pointer forward until we find a letter/number
        while l < r and not s[l].isalnum():
            l += 1
        
        # 2. Move Right pointer backward until we find a letter/number
        while r > l and not s[r].isalnum():
            r -= 1
        
        # 3. Compare characters (case-insensitive)
        if s[l].lower() != s[r].lower():
            return False
        
        # 4. Update pointers after a successful match
        l, r = l + 1, r - 1
        
    return True