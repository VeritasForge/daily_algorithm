from src.leetcode.implement_queue_using_stacks_232 import MyQueue


def test_my_queue_example1() -> None:
    """
    Input: ["MyQueue", "push", "push", "peek", "pop", "empty"]
           [[], [1], [2], [], [], []]
    Output: [null, null, null, 1, 1, false]
    """
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() is False


def test_my_queue_empty() -> None:
    queue = MyQueue()
    assert queue.empty() is True
    queue.push(1)
    assert queue.empty() is False
    queue.pop()
    assert queue.empty() is True


def test_my_queue_fifo_order() -> None:
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
