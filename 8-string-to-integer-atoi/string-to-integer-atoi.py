
class Solution(object):
    def myAtoi(self, s):
        lis = ['0','1','2','3','4','5','6','7','8','9','-','+']
        a = 1
        res = ""
        ab = s.strip()

        if len(ab) == 0:
            return 0

        if ab[0] == '-':
            a = -1

        for i in range(len(ab)):
            if ab[i] in lis:

                if ab[i] == '-' or ab[i] == '+':
                    if i != 0:
                        break
                    else:
                        continue

                res += ab[i]
            else:
                break

        if len(res) == 0:
            return 0

        num = 0
        for ch in res:
            num = num * 10 + (ord(ch) - ord('0'))

        num = a * num

        if num > 2**31 - 1:
            return 2**31 - 1
        if num < -(2**31):
            return -(2**31)

        return num