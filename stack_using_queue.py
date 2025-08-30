from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        
        # Rotate until x comes to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Driver Code

if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.top())  # 3
    print(stack.pop())  # 3
    print(stack.top())  # 2
    print(stack.pop())  # 2
    print(stack.empty())  # False
    print(stack.pop())  # 1
    print(stack.empty())  # True
