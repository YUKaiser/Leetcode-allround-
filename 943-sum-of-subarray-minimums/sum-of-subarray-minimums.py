class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        NSL=[-1]*len(arr)
        NSR=[len(arr)]*len(arr)
        L_stack=[]
        R_stack=[]
        for i in range(len(arr)):
            while L_stack and arr[L_stack[-1]]>arr[i]:
                L_stack.pop()
            if L_stack:
                NSL[i]=L_stack[-1]
            L_stack.append(i)
        NSR=[len(arr)]*len(arr)
        R_stack=[]
        for j in range(len(arr)-1,-1,-1):
            while R_stack and arr[j]<=arr[R_stack[-1]]:
                R_stack.pop()
            if R_stack:
                NSR[j]=R_stack[-1]
            R_stack.append(j)
        mini_sum=0
        for i in range(len(arr)):
            left_side_min=i-NSL[i]
            right_side_min=NSR[i]-i
            mini_sum=(mini_sum+left_side_min*right_side_min*arr[i])%MOD
        return mini_sum

        

