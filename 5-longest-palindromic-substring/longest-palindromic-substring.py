class Solution(object):
   def longestPalindrome(self, s):
    longest = ""
    
    for i in range(len(s)):
        # We start searching from the end of the string for every 'i'
        for j in range(len(s) - 1, i - 1, -1):
            # Check if the substring s[i:j+1] is a palindrome
            # Using s[i:j+1] == s[i:j+1][::-1] is the simplest way in Python
            substring = s[i:j+1]
            
            if substring == substring[::-1]:
                # If this one is longer than our current best, save it
                if len(substring) > len(longest):
                    longest = substring
                # Since we are checking from the end (j), the first palindrome 
                # we find for this 'i' is the longest possible for this start point.
                # So we can break the inner loop and move to i+1.
                break
                
    return longest
                    




        