class Solution(object):
    def myAtoi(self, s):
        a = ""
        # 1. We need to handle leading whitespace first so it doesn't 
        # interfere with our sign/digit logic inside the loop.
        s = s.lstrip() 
        
        for i in range(len(s)):
            # Check for digits
            if s[i].isdigit():
                a = a + s[i]
            
            # Check for sign (only if it's the very first character)
            elif s[i] in ["-", "+"] and i == 0:
                a = a + s[i]
            
            # If we hit anything else (space, letter, or a second sign), we STOP.
            else:
                break 

        # Final checks before returning
        if a == "" or a == "-" or a == "+":
            return 0
            
        # Convert to int and handle the 32-bit limits
        res = int(a)
        
        if res > 2147483647: return 2147483647
        if res < -2147483648: return -2147483648
        
        return res