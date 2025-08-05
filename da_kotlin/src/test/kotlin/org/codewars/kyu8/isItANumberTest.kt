package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class IsItANumberTest {

    private fun sampleTestCases() = listOf(
        Arguments.of(3, 3, 4, false),
        Arguments.of(12, 3, 4, true),
        Arguments.of(8, 3, 4, false),
        Arguments.of(48, 3, 4, true),
        Arguments.of(100, 5, 10, true),
    )

    @ParameterizedTest
    @MethodSource("sampleTestCases")
    fun `should return correct result for sample tests`(n: Int, x: Int, y: Int, expected: Boolean) {
        assertEquals(expected, isDigit(n, x, y))
    }
}
