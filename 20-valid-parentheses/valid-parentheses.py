class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st_k=[]
        for ch in s:
            if (ch in '{[('):
                st_k.append(ch)
    
            else:
                if not st_k:
                    return False
                a=st_k.pop()
                if ((a+ch) not in ("{}","[]","()")):
                    return False
        return len(st_k)==0