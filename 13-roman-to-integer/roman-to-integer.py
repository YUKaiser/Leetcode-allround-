class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        i=0
        dicta_s = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9,'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 
                    'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        while i<len(s):
            if s[i:i+2] in dicta_s:

                sum=dicta_s[s[i:i+2]]+sum
                i=i+2
            else:
                sum=dicta_s[s[i]]+sum
                i=i+1
        
        return sum