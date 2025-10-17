package org.codewars.kyu7

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class HighestAndLowestTest {

    @ParameterizedTest
    @MethodSource("testCases")
    fun `highAndLow should return the highest and lowest numbers`(numbers: String, expected: String) {
        assertEquals(expected, highAndLow(numbers))
    }

    private fun testCases(): List<Arguments> {
        return listOf(
            Arguments.of("1 2 3 4 5", "5 1"),
            Arguments.of("1 2 -3 4 5", "5 -3"),
            Arguments.of("1 9 3 4 -5", "9 -5"),
            Arguments.of("42", "42 42"),
            Arguments.of("-1 -2 -3 -4 -5", "-1 -5"),
            Arguments.of("8 3 -5 42 -1 0 0 -9 4 7 4 -4", "42 -9")
        )
    }
}
