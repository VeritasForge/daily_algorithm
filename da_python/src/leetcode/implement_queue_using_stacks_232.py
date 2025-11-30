# https://leetcode.com/problems/implement-queue-using-stacks/
# 232. Implement Queue using Stacks
#
# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal queue
# (push, peek, pop, and empty).
#
# Implement the MyQueue class:
# - void push(int x): Pushes element x to the back of the queue.
# - int pop(): Removes the element from the front of the queue and returns it.
# - int peek(): Returns the element at the front of the queue.
# - boolean empty(): Returns true if the queue is empty, false otherwise.
#
# Notes:
# - You must use only standard operations of a stack (push to top, peek/pop from top,
#   size, and is empty).
# - You may simulate a stack using a list as long as you use only standard stack operations.
#
# Follow-up: Can you implement the queue such that each operation is amortized O(1)?


class MyQueue:
    def __init__(self) -> None:
        self._stack_in: list[int] = []
        self._stack_out: list[int] = []

    def push(self, x: int) -> None:
        self._stack_in.append(x)

    def pop(self) -> int:
        self._transfer()
        return self._stack_out.pop()

    def peek(self) -> int:
        self._transfer()
        return self._stack_out[-1]

    def empty(self) -> bool:
        return not (self._stack_in or self._stack_out)

    def _transfer(self):
        if self._stack_out:
            return

        while self._stack_in:
            self._stack_out.append(self._stack_in.pop())
