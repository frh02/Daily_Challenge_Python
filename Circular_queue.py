'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

'''
#SOLUTION:

class MyCircularQueue(object):
    def __init__(self, k):
        self.head = self.tail = self.size = 0
        self.arr = [0] * k

    def enQueue(self, value):
        if self.isFull():
            return False
        self.arr[self.tail] = value
        self.tail = (self.tail + 1) % len(self.arr)
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % len(self.arr)
        self.size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.arr[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.arr[self.tail-1]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == len(self.arr)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
