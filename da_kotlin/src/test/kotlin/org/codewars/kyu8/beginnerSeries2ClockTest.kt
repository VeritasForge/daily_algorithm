package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class BeginnerSeries2ClockTest {

    private fun testCases(): List<Arguments> = listOf(
        Arguments.of(0, 1, 1, 61000),
        Arguments.of(1, 1, 1, 3661000),
        Arguments.of(0, 0, 0, 0),
        Arguments.of(1, 0, 1, 3601000),
        Arguments.of(1, 0, 0, 3600000),
        Arguments.of(23, 59, 59, 86399000)
    )

    @ParameterizedTest(name = "past({0}, {1}, {2}) should be {3}")
    @MethodSource("testCases")
    fun `should return the time since midnight in milliseconds`(h: Int, m: Int, s: Int, expected: Int) {
        assertEquals(expected, past(h, m, s))
    }
}
