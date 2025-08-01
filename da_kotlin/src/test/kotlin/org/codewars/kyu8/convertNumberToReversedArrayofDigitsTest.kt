package org.codewars.kyu8

import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.api.Assertions.assertArrayEquals
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class convertNumberToReversedArrayofDigitsTest {

    fun methodSource() = listOf(
        Arguments.of(35231, intArrayOf(1, 3, 2, 5, 3)),
        Arguments.of(0, intArrayOf(0)),
    )

    @ParameterizedTest
    @MethodSource("methodSource")
    fun `convert number to reversed array of digits`(n: Long, expected: IntArray) {
        // When:
        val actual = digitize(n)

        // Then:
        assertArrayEquals(actual, expected)
    }
}
