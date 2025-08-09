package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class YouCantCodeUnderPressure1Test {
    @ParameterizedTest
    @MethodSource("testCases")
    fun testFixed(expected: Int, n: Int) {
        assertEquals(expected, doubleInteger(n))
    }

    private fun testCases() = listOf(
        Arguments.of(4, 2),
        Arguments.of(10, 5),
        Arguments.of(20, 10),
        Arguments.of(200, 100)
    )
}
