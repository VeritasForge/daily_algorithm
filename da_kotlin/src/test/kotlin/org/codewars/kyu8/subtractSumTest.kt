package org.codewars.kyu8

import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import kotlin.test.assertEquals

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class SubtractSumTest {

    @ParameterizedTest
    @MethodSource("subtractSumArguments")
    fun testSubtractSum(expected: String, n: Int) {
        assertEquals(expected, subtractSum(n))
    }

    private fun subtractSumArguments(): List<Arguments> {
        return listOf(
            Arguments.of("apple", 10),
            Arguments.of("apple", 325)
        )
    }
}
