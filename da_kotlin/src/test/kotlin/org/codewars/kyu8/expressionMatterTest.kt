package org.codewars.kyu8

import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import kotlin.test.assertEquals

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ExpressionMatterTest {

    @ParameterizedTest(name = "a={0}, b={1}, c={2}, expected={3}")
    @MethodSource("testCases")
    fun `expressionsMatter should return the maximum possible result`(a: Int, b: Int, c: Int, expected: Int) {
        assertEquals(expected, expressionsMatter(a, b, c))
    }

    private fun testCases(): List<Arguments> {
        return listOf(
            Arguments.of(2, 1, 2, 6),
            Arguments.of(1, 2, 3, 9),
            Arguments.of(1, 1, 1, 3),
            Arguments.of(1, 3, 1, 5),
            Arguments.of(2, 2, 2, 8),
            Arguments.of(5, 1, 3, 20),
            Arguments.of(3, 5, 7, 105),
            Arguments.of(5, 6, 1, 35),
            Arguments.of(1, 6, 1, 8),
            Arguments.of(2, 6, 1, 14),
            Arguments.of(6, 7, 1, 48),
            Arguments.of(2, 10, 3, 60),
            Arguments.of(1, 8, 3, 27),
            Arguments.of(1, 1, 10, 20),
            Arguments.of(9, 1, 1, 18),
            Arguments.of(10, 5, 6, 300),
            Arguments.of(1, 10, 1, 12)
        )
    }
}
