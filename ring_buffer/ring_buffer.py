class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current == self.capacity:
      self.current = 0
    self.storage[self.current] = item
    self.current += 1
    print(f'ARRAY: {self.storage}')

  def get(self):
    list = []
    for item in self.storage:
      if item != None:
        list.append(item)
    return list