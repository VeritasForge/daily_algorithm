package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertArrayEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class CountOfPositivesSumOfNegativesTest {

    private fun testCases(): List<Arguments> {
        return listOf(
            Arguments.of(
                arrayOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15),
                arrayOf(10, -65)
            ),
            Arguments.of(
                arrayOf(0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14),
                arrayOf(8, -50)
            ),
            Arguments.of(
                emptyArray<Int>(),
                emptyArray<Int>()
            ),
            Arguments.of(
                null,
                emptyArray<Int>()
            )
        )
    }

    @ParameterizedTest
    @MethodSource("testCases")
    fun test(input: Array<Int>?, expected: Array<Int>) {
        assertArrayEquals(expected, countPositivesSumNegatives(input))
    }
}
