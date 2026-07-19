class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stk=[]
        n=len(asteroids)
        stk.append(asteroids[0])
        for i in range(1,n):
            alive=True
            while stk and asteroids[i]<0 and stk[-1]>0:
                if abs(asteroids[i])==stk[-1]:
                    stk.pop()
                    alive=False
                    break
                elif abs(asteroids[i])>stk[-1]:
                    stk.pop()
                else:
                    alive=False
                    break
            if alive:

                stk.append(asteroids[i])
        return stk