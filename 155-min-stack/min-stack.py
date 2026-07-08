class MinStack(object):

    def __init__(self):
        self.items=[]
        self.mini=float('inf')

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.items.append(value)
        self.mini=min(value,self.mini)

    def pop(self):
        """
        :rtype: None
        """
        if self.Empty():
            return -1
        self.a=self.items.pop()
        if self.Empty():
            self.mini=float('inf')
        elif self.a==self.mini:
            self.mini=min(self.items)

        return self.a

    def top(self):
        """
        :rtype: int
        """
        if self.Empty():
            return 0
        return self.items[-1]
        

    def getMin(self):
        """
        :rtype: int
     
        """
        if self.Empty():
            return -1
        return self.mini
    def Empty(self):
        return len(self.items)==0   


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()