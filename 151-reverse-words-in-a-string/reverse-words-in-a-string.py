class Solution(object):
    def reverseWords(self, s):
        word=s.split()
        word.reverse()
        result=" ".join(word)
        return result
        
        """
        :type s: str
        :rtype: str
        """
        