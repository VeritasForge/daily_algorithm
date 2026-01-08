import pytest

from src.common.linked_list import create_linked_list, create_list
from src.leetcode.reverse_linked_list_206 import reverse_list


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ],
)
def test_reverse_list(input_list: list[int], expected: list[int]):
    head = create_linked_list(input_list)
    result = reverse_list(head)
    assert create_list(result) == expected
