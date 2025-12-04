import pytest

from src.common.linked_list import (
    create_linked_list_with_cycle,
)
from src.leetcode.linked_list_cycle_141 import has_cycle


@pytest.mark.parametrize(
    "values, pos, expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
    ],
)
def test_has_cycle(values: list[int], pos: int, expected: bool) -> None:
    head = create_linked_list_with_cycle(values, pos)
    assert has_cycle(head) == expected
