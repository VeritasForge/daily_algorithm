import pytest

from src.common.linked_list import create_linked_list
from src.leetcode.merge_two_sorted_list_21 import ListNode, merge_two_list


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (
            create_linked_list([1, 2, 4]),
            create_linked_list([1, 3, 4]),
            [1, 1, 2, 3, 4, 4],
        ),
        (create_linked_list([]), create_linked_list([]), []),
        (create_linked_list([]), create_linked_list([0]), [0]),
    ],
)
def test_merge_two_list(
    a: ListNode | None, b: ListNode | None, expected: list[int] | None
):
    # When:
    result = merge_two_list(a, b)

    # Then:
    result_as_list = []
    while result:
        result_as_list.append(result.val)
        result = result.next

    assert result_as_list == expected
