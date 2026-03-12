class Solution(object):
    def minDays(self, bloomDay, m, k):
        min_day=min(bloomDay)
        max_day=max(bloomDay)
        result_day=-1
        while min_day<=max_day:
            mid=(min_day+max_day)//2
            if(self.checkbloom(mid,bloomDay,m,k)>=m):
                result_day=mid
                max_day=mid-1
            else:
                min_day=mid+1
        return result_day
    def checkbloom(self,mid,bloomDay,m,k):
        count=0
        t_bq=0
        for day in bloomDay:
           
            if day<=mid:
                count=count+1
            else:
                count=0
            if(count==k):
                t_bq=t_bq+1
                count=0
        return t_bq
                        


        
      

        

        
        