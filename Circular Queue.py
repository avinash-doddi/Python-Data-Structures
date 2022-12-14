class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [];
        self.size = 0;
        self.maxsize = k;

    def enQueue(self, value: int) -> bool:
        if (self.size == self.maxsize): return False
        self.queue.append(value);
        self.size += 1;
        return True

    def deQueue(self) -> bool:
        if (self.size == 0): return False
        del self.queue[0];
        self.size -= 1;
        return True
        
    def Front(self) -> int:
        if (self.size == 0): return -1;
        return self.queue[0];

    def Rear(self) -> int:
        if (self.size == 0): return -1;
        return self.queue[-1];

    def isEmpty(self) -> bool:
        if (self.size == 0): return True
        return False;

    def isFull(self) -> bool:
        if (self.size == self.maxsize): return True
        return False
        


# MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
