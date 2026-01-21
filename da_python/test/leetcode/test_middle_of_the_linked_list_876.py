import pytest

from src.common.linked_list import ListNode, create_linked_list, create_list
from src.leetcode.middle_of_the_linked_list_876 import middle_node


@pytest.mark.parametrize(
    "head, expected",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
    ],
)
def test_middle_node(head: list[int], expected: list[int]) -> None:
    head_node = create_linked_list(head)
    result = middle_node(head_node)
    assert create_list(result) == expected
