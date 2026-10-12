import math

class Solution(object):
    def maxPrimes(self, n, s):
        """
        :type n: int
        :type s: int
        :rtype: List[int]
        """
        if n < 2 or s <= 0:
            return []
            
        
        
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if prime[i] == True:
                for j in range(i * i, n + 1, i):
                    prime[j] = False
                 
    

        final = []
        c = 0
        for i in range(2, n + 1):
            if prime[i]:
                if c + i <= s:
                    final.append(i)
                    c += i
                else:
                    break
                    
        return final
