package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class SimpleMultiplicationTest {

    private fun testCases() = listOf(
        arrayOf(1, 9),
        arrayOf(2, 16),
        arrayOf(3, 27),
        arrayOf(4, 32),
        arrayOf(5, 45),
        arrayOf(8, 64),
        arrayOf(10, 80),
        arrayOf(0, 0)
    )

    @ParameterizedTest
    @MethodSource("testCases")
    fun `simpleMultiplication should return the correct result`(input: Int, expected: Int) {
        assertEquals(expected, simpleMultiplication(input))
    }
}
