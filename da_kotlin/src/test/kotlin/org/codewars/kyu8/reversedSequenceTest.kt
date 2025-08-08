package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ReversedSequenceTest {

    @ParameterizedTest
    @MethodSource("testCases")
    fun `reversedSequence should return the correct reversed sequence`(n: Int, expected: List<Int>) {
        assertEquals(expected, reversedSequence(n))
    }

    private fun testCases(): List<Arguments> {
        return listOf(
            Arguments.of(5, listOf(5, 4, 3, 2, 1)),
            Arguments.of(3, listOf(3, 2, 1)),
            Arguments.of(1, listOf(1))
        )
    }
}
