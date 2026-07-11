# https://leetcode.com/problems/implement-stack-using-queues/
# 225. Implement Stack using Queues
#
# Implement a last-in-first-out (LIFO) stack using only two queues.
# The implemented stack should support all the functions of a normal stack
# (push, top, pop, and empty).
#
# Implement the MyStack class:
# - void push(int x): Pushes element x to the top of the stack.
# - int pop(): Removes the element on the top of the stack and returns it.
# - int top(): Returns the element on the top of the stack.
# - boolean empty(): Returns true if the stack is empty, false otherwise.
#
# Notes:
# - You must use only standard operations of a queue (push to back,
#   peek/pop from front, size, and is empty).
# - You may simulate a queue using a list or deque as long as you use only
#   a queue's standard operations.
#
# Constraints:
# - 1 <= x <= 9
# - At most 100 calls will be made to push, pop, top, and empty.
# - All the calls to pop and top are valid.
#
# Follow-up: Can you implement the stack using only one queue?


from collections import deque


class MyStack:
    def __init__(self) -> None:
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
