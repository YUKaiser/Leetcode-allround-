class Robot(object):

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.pos = 0
        self.perimeter = 2 * (width - 1) + 2 * (height - 1)
        self.moved = False

    def step(self, num):
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter
        # If we land on 0 after moving, it means we completed a full lap
        # and are facing South at (0,0).
        if self.pos == 0:
            self.pos = 0 

    def getPos(self):
        curr = self.pos
        if curr < self.w:
            return [curr, 0]
        curr -= (self.w - 1)
        if curr < self.h:
            return [self.w - 1, curr]
        curr -= (self.h - 1)
        if curr < self.w:
            return [self.w - 1 - curr, self.h - 1]
        curr -= (self.w - 1)
        return [0, self.h - 1 - curr]

    def getDir(self):
        # Initial state before any movement
        if not self.moved or self.pos == 0 and self.moved:
            # Special case: (0,0) after movement is always South
            return "South" if self.moved else "East"
            
        curr = self.pos
        if 1 <= curr <= self.w - 1:
            return "East"
        if self.w <= curr <= self.w + self.h - 2:
            return "North"
        if self.w + self.h - 1 <= curr <= 2 * self.w + self.h - 3:
            return "West"
        return "South"