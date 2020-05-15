class RingBuffer:
    def __init__(self, capacity):
        self.current = 0
        self.capacity = capacity
        self.storage = [None] * capacity
        
    def append(self, value):
        self.storage[self.current] = value
        self.current += 1
        if self.current == self.capacity:
            self.current = 0
            
    def get(self):
        return [x for x in self.storage if x is not None]
