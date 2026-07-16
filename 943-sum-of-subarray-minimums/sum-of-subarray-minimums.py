class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)

        NSL = [-1] * n
        NSR = [n] * n

        L_stack = []
        R_stack = []

        # Previous Smaller (Strictly Smaller)
        for i in range(n):
            while L_stack and arr[L_stack[-1]] > arr[i]:
                L_stack.pop()

            if L_stack:
                NSL[i] = L_stack[-1]

            L_stack.append(i)

        # Next Smaller or Equal
        for i in range(n - 1, -1, -1):
            while R_stack and arr[i] <= arr[R_stack[-1]]:
                R_stack.pop()

            if R_stack:
                NSR[i] = R_stack[-1]

            R_stack.append(i)

        ans = 0

        for i in range(n):
            left = i - NSL[i]
            right = NSR[i] - i
            ans = (ans + left * right * arr[i]) % MOD

        return ans