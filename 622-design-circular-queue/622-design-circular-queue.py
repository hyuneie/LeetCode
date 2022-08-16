class MyCircularQueue:
    def __init__(self, k: int):
        self.Length = k
        self.Queue = [None for i in range(k)]
        self.FrontIDX = 0
        self.RearIDX = 0
        self.Full = False
    def enQueue(self, value: int) -> bool:
        if not self.Full:
            self.Queue[self.RearIDX] = value
            self.RearIDX += 1
            if self.RearIDX == self.Length:
                self.RearIDX = 0
            if self.RearIDX == self.FrontIDX:
                self.Full = True
            return True
        return False
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.Full = False
        self.FrontIDX += 1
        if self.FrontIDX == self.Length:
            self.FrontIDX = 0
        return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.Queue[self.FrontIDX]
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.Queue[self.RearIDX-1]
    def isEmpty(self) -> bool:
        return self.Full == False and self.RearIDX == self.FrontIDX
    def isFull(self) -> bool:
        return self.Full


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()