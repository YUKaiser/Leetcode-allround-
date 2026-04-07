class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        i = 0
        # Your dictionary is perfect for this approach
        dicta_s = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 
            'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 
            'CM': 900, 'M': 1000
        }
        
        while i < len(s):
            # 1. Try to grab a 2-character slice (e.g., "IV")
            # 2. Check if it's in our dictionary
            if i + 1 < len(s) and s[i:i+2] in dicta_s:
                total += dicta_s[s[i:i+2]]
                i += 2  # Jump forward 2 steps because we used 2 characters
            else:
                # 3. Otherwise, just process the single character
                total += dicta_s[s[i]]
                i += 1  # Move forward 1 step
                
        return total