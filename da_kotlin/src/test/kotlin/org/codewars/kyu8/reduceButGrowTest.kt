package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ReduceButGrowTest {

    private fun basicTests(): List<Arguments> {
        return listOf(
            Arguments.of(6, intArrayOf(1, 2, 3)),
            Arguments.of(16, intArrayOf(4, 1, 1, 1, 4)),
            Arguments.of(64, intArrayOf(2, 2, 2, 2, 2, 2))
        )
    }

    @ParameterizedTest
    @MethodSource("basicTests")
    fun test(expected: Int, arr: IntArray) {
        assertEquals(expected, grow(arr))
    }
}
