

class UniversalContainer:

    def __init__(self): # constructor for empty container
        self.capacity_ = 1 # we reserve memory for at least one item
        self.data_ = [None]*self.capacity_ # the internal memory
        self.size_ = 0  # no item has been inserted yet

    def size(self):
        return self.size_

    def capacity(self):
        return self.capacity_

    def push(self, item): # add item at the end
        if self.capacity_ == self.size_: # internal memory is full ...
            # your code to enlarge the memory:
            self.data_ = self.data_ * 2
            self.capacity_ = self.capacity_ * 2
        self.data_[self.size_] = item
        self.size_ += 1

    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        output = self.data_.pop(0)
        self.size_ -= 1
        self.capacity_ -=  1
        return output

    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popLast() on empty container")
        output = self.data_.pop(self.size_-1)
        self.size_ -= 1
        self.capacity_ -=  1
        return output

    def __getitem__(self, index): # __getitem__ implements v = c[index]
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        return self.data_[index]

    def __setitem__(self, index, v): # __setitem__ implements c[index] = v
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        self.data_[index] = v

    def first(self):
        return self.data_[0]

    def last(self):
        return self.data_[self.size_ - 1]

def testContainer():
    a = UniversalContainer()
    b = UniversalContainer()
    assert a.size() == 0, "Size of the new container is not zero!"
    assert a.size() <= a.capacity(), "Size is bigger than the capacity"
    memory = a.size()
    a.push(5)
    assert a.size() == memory+1, "Size does not inkrement after push"
    assert a.last() == 5, "The new element is not at the rigth position"
    b = a
    a.push(8)
    assert a[0] == 5, "The other elements changed after the push"
    a.popLast()
    assert a == b, "Error in popLast or push"
    a.push(9)
    memory = a.size()
    a[0] = 6
    assert a.size() == memory, "Size changed Error!"
    assert a[0] == 6, "Error: Wrong element"
    assert a[1] == 9, "Error: Elements Changed"
    memory = a.size()
    a.popLast()
    assert a.size() == memory-1, "Error: Size changed incorrect"
    assert a[0] == 6, "Wrong Elements Changed"
    a.push(66)
    memory = a.size()
    a.popFirst()
    assert a.size() == memory-1, "Error: Size changed"
    assert a.first()==a[0] and a.last()==a[a.size()-1], "Error illegal Functions"


testContainer()
c = UniversalContainer()
print("Start")
c.push(5)
c.push(10)
c.push(15)
print("[0]:", c[0])
print("[1]:", c[1])
print("[2]:", c[2])
print("size():", c.size())
print("capacity():", c.capacity())
print("First Value was", c.popFirst())
print("Last Value was", c.popLast())
print(c.size())
print(c.capacity())
print(c[0])
c[0] = 20
print(c[0])
c.push(33)
print("First Element: ", c.first())
print("Last Element: ", c.last())
print("Ende")
