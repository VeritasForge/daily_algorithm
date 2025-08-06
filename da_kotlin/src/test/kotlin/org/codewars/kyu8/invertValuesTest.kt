package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertArrayEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class InvertValuesTest {

    private fun testData(): List<Arguments> = listOf(
        Arguments.of(intArrayOf(1, 2, 3, 4, 5), intArrayOf(-1, -2, -3, -4, -5)),
        Arguments.of(intArrayOf(1, -2, 3, -4, 5), intArrayOf(-1, 2, -3, 4, -5)),
        Arguments.of(intArrayOf(), intArrayOf()),
        Arguments.of(intArrayOf(0), intArrayOf(0))
    )

    @ParameterizedTest
    @MethodSource("testData")
    fun `test invert`(input: IntArray, expected: IntArray) {
        assertArrayEquals(expected, invert(input))
    }
}
