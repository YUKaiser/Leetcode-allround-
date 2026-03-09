class Solution(object):
    def removeOuterParentheses(self, s):
        emp_str=""
        count=0
        for ch in s:
            if ch=='(':
                count=count+1
                if count>1:
                    emp_str += ch
            else:
                count=count-1
                if count>0:
                    emp_str += ch
        return emp_str
        
        