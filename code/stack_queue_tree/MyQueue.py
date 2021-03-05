# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
# 实现 MyQueue 类：
from queue import LifoQueue


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = LifoQueue()
        self.out_stack = LifoQueue()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.put(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.out_stack.empty():
            while not self.in_stack.empty():
                self.out_stack.put(self.in_stack.get())
        return self.out_stack.get()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.out_stack.empty():
            while not self.in_stack.empty():
                self.out_stack.put(self.in_stack.get())
        self.out_stack.put(x := self.out_stack.get())
        return x

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.out_stack.empty():
            return self.in_stack.empty()
        return False


if __name__ == '__main__':
    array = [1, 2]
    obj = MyQueue()
    obj.push(array[0])
    obj.push(array[1])
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
