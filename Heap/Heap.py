class Heap:
    def __init__(self):
        # storage starts with an unused 0 to make
        # integer division simpler later on
        self.storage = [0]
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        self._bubble_up(self.size)

    def delete(self):
        self.storage[1], self.storage[-1] = self.storage[-1], self.storage[1]
        deleted_value = self.storage.pop(-1)
        self.size -= 1
        self._sift_down_(1)
        return deleted_value

    def get_max(self):
        return self.storage[1]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        # my two part base case for recursion:
        # if parent is greater than child or if index less than or equal to one
        if self.storage[index] < self.storage[index//2] or index <= 1:
            return
        else:
            # swap the parent/child values
            self.storage[index], self.storage[index //
                                              2] = self.storage[index//2], self.storage[index]
            # recursive call
            return self._bubble_up(index//2)

    def _sift_down_(self, index):
        left_child = index * 2
        right_child = (index * 2) + 1
        if left_child > self.size:
            return
        if right_child <= self.size:
            if self.storage[index] < self.storage[left_child] or self.storage[index] < self.storage[right_child]:
                largest_child = right_child if (
                    self.storage[right_child] > self.storage[left_child]) else left_child
                self.storage[index], self.storage[largest_child] = self.storage[largest_child], self.storage[index]
                return self._sift_down_(largest_child)
            else:
                return
        else:
        if self.storage[index] < self.storage[left_child]:
            self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
            return self._sift_down_(left_child)
        else:
            return
