class Solution(object):
    def evalRPN(self, tokens):
        sta_k = []

        for ch in tokens:
            if ch not in ('+', '-', '*', '/'):
                sta_k.append(int(ch))
            else:
                b = sta_k.pop()
                a = sta_k.pop()
                sta_k.append(self.calculate(a, ch, b))

        return sta_k[0]

    def calculate(self, a, ch, b):
        if ch == '+':
            return a + b
        elif ch == '-':
            return a - b
        elif ch == '*':
            return a * b
        elif ch == '/':
            return int(float(a) / b)