class Solution(object):
    def asteroidCollision(self, asteroids):
        stk = []

        for asteroid in asteroids:
            if stk and asteroid < 0 and stk[-1] > 0:
                self.check(asteroid, stk)
            else:
                stk.append(asteroid)

        return stk

    def check(self, out, stk):

        if not stk:
            stk.append(out)
            return

        top = stk.pop()

        if top < 0:
            stk.append(top)
            stk.append(out)
            return

        if abs(out) > top:
            self.check(out, stk)

        elif abs(out) == top:
            return

        else:
            stk.append(top)
            return