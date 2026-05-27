class Solution(object):
    def sortSentence(self, s):
        r=s.split()
        ans=[""]*len(r)
        for i in range(0,len(r)):
            a=int(r[i][len(r[i])-1])-1
            ans[a]=r[i][:-1]
        return " ".join(ans)

        