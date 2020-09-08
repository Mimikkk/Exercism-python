from collections import deque
class CircularBuffer(object):
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.buffer_queue = deque()

    def read(self):
        if not self.buffer_queue: raise ValueError('Empty buffer')
        return self.buffer_queue.popleft()

    def write(self, data):
        if len(self.buffer_queue) >= self.capacity: raise ValueError('Full buffer')
        self.buffer_queue.append(data)

    def overwrite(self, data):
        if len(self.buffer_queue) < self.capacity:
            self.buffer_queue.append(data)
        else:
            self.buffer_queue.popleft()
            self.buffer_queue.append(data)

    def clear(self):
        return self.buffer_queue.clear()
