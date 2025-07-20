import pytest

from src.leetcode.merge_two_sorted_list_21 import ListNode, node_to_list


def create_node(*args) -> ListNode | None:
    if not args:
        return None

    result = head = ListNode(val=args[0])
    for val in args[1:]:
        head.next_node = head = ListNode(val=val)
    return result


@pytest.mark.parametrize(
    "arr",
    [
        [1, 2, 3],
        [1, 2],
        [1, 1],
        [1],
        [],
    ],
)
def test_create_node(arr):
    # When:
    result = create_node(*arr)

    # Then:
    for v in arr:
        assert result.val == v
        result = result.next_node


@pytest.mark.parametrize(
    "node, expected",
    [
        (create_node(1, 2, 3), [1, 2, 3]),
        (create_node(1, 1), [1, 1]),
        (None, []),
    ],
)
def test_node_to_list(node: ListNode | None, expected: list[int] | None):
    # When:
    result = node_to_list(node)

    # Then:
    assert result == expected


# @pytest.mark.parametrize(
#     "a, b, expected",
#     [
#         (create_node(1, 2, 4), create_node(1, 3, 4), [1, 1, 2, 3, 4, 4]),
#         # (create_node(), create_node(), [1, 2, 3, 4, 4]),
#     ]
# )
# def test_merge_two_list(a: ListNode | None, b: ListNode | None, expected: list[int] | None):
#     # When:
#     result = merge_two_list(a, b)
#
#     # Then:
#     result_as_list = []
#     while result:
#         result_as_list.append(result.val)
#         result = result.next_node
#
#     assert result_as_list == expected
