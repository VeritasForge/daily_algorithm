from src.leetcode.implement_stack_using_queues_225 import MyStack


def test_my_stack_example1() -> None:
    """
    LeetCode 기본 예제
    Input: ["MyStack", "push", "push", "top", "pop", "empty"]
           [[], [1], [2], [], [], []]
    Output: [null, null, null, 2, 2, false]
    """
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.empty() is False


# 보강 - 엣지 케이스
def test_my_stack_empty_initially() -> None:
    stack = MyStack()
    assert stack.empty() is True


def test_my_stack_becomes_empty_after_pop() -> None:
    stack = MyStack()
    stack.push(1)
    assert stack.empty() is False
    stack.pop()
    assert stack.empty() is True


def test_my_stack_single_element() -> None:
    stack = MyStack()
    stack.push(9)
    assert stack.top() == 9
    assert stack.pop() == 9
    assert stack.empty() is True


# 보강 - 예외 케이스 (LIFO 순서 검증: 큐를 잘못 쓰면 FIFO로 새는 실수가 흔함)
def test_my_stack_lifo_order() -> None:
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


# 보강 - 추가 검증
def test_my_stack_top_does_not_remove_element() -> None:
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.top() == 1


def test_my_stack_interleaved_push_pop() -> None:
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 1
    assert stack.empty() is True
