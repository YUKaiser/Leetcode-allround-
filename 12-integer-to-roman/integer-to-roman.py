class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
        s=""
        while num>0:
            for i in range(len(res)):

                if num>=res[i][0]:
                    s+=res[i][1]
                    num=num-res[i][0]
                    break
                else:
                    continue

        return s