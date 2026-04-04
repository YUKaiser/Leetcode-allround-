class Solution(object):
    def rotateString(self, s, goal):
        st = list(s)
        g = list(goal)

        for i in range(len(st)):
            if st[i] == g[0]:
                rotated = st[i:] + st[:i]
                if rotated == g:
                    return True

        return False