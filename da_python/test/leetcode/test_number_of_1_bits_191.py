import pytest

from src.leetcode.number_of_1_bits_191 import hamming_weight

pytestmark = pytest.mark.skip(reason="WIP")


@pytest.mark.skip("test")
@pytest.mark.parametrize(
    "n, expected",
    [
        (11, 3),  # 00000000000000000000000000001011
        (128, 1),  # 00000000000000000000000010000000
        (2147483645, 30),  # 01111111111111111111111111111101
    ],
)
def test_hamming_weight(n: int, expected: int):
    assert hamming_weight(n) == expected
