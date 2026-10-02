class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        a=1
        for i in range(n):
            res.append((a))
            a+=1
        for j in range(len(res)):
            if res[j]%3==0 and res[j]%5==0:
                res[j]="FizzBuzz"
            elif res[j]%3==0:
                res[j]="Fizz"
            elif res[j]%5==0:
                res[j]="Buzz"
            else:
                res[j]=str(res[j])
        return res

    