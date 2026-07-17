class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NMaxL=[-1]*len(nums)
        NMaxR=[len(nums)]*len(nums)
        left_st=[]
        right_st=[]
        Maxi_sum=0
        for i in range(len(nums)):
            while left_st and nums[left_st[-1]]<=nums[i]:
                left_st.pop()
            if left_st:
                NMaxL[i]=left_st[-1]
            left_st.append(i)
        for i in range(len(nums)-1,-1,-1):
            while right_st and nums[i]>nums[right_st[-1]]:
                right_st.pop()
            if right_st:
                NMaxR[i]=right_st[-1]
            right_st.append(i)
        
        for i in range(len(nums)):
            left=i-NMaxL[i]
            right=NMaxR[i]-i
            Maxi_sum=(Maxi_sum+(left*right*nums[i]))

        NML=[-1]*len(nums)
        NMR=[len(nums)]*len(nums)
        l_st=[]
        r_st=[]
        Mini_sum=0
        for i in range(len(nums)):
            while l_st and nums[l_st[-1]]>=nums[i]:
                l_st.pop()
            if l_st:
                NML[i]=l_st[-1]
            l_st.append(i)
        for i in range(len(nums)-1,-1,-1):
            while r_st and nums[i]<nums[r_st[-1]]:
                r_st.pop()
            if r_st:
                NMR[i]=r_st[-1]
            r_st.append(i)
        
        for i in range(len(nums)):
            left=i-NML[i]
            right=NMR[i]-i
            Mini_sum=(Mini_sum+(left*right*nums[i]))
        return Maxi_sum-Mini_sum