'''9. Palindrome Number
Solved
Easy
Given an integer x, return true if x is a 
palindrome
, and false otherwise.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Constraints:
-231 <= x <= 231 - 1 
Follow up: Could you solve it without converting the integer to a string?'''
#solution 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
      y=str(x)
      z=y[::-1]
      if(z==y):
        return True
      else:
        return False
#Solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=x
        y=0
        while(x>0):
            y=y*10+x%10
            x=x//10
        if(a==y):
            return True
        else:
            return False
