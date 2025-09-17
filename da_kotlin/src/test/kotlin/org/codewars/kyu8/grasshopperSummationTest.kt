
package org.codewars.kyu8

import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import kotlin.test.assertEquals

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class GrasshopperSummationTest {

    private fun summationTestCases(): List<Arguments> {
        return listOf(
            Arguments.of(1, 1),
            Arguments.of(2, 3),
            Arguments.of(8, 36),
            Arguments.of(100, 5050)
        )
    }

    @ParameterizedTest(name = "summation({0}) should return {1}")
    @MethodSource("summationTestCases")
    fun `test summation`(n: Int, expected: Int) {
        assertEquals(expected, summation(n))
    }
}
