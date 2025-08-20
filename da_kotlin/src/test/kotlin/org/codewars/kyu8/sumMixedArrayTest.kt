package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.MethodSource
import org.junit.jupiter.api.TestInstance

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class SumMixedArrayTest {

    private fun testCases() = listOf(
        Pair(listOf(9, 3, "7", "3"), 22),
        Pair(listOf("5", "0", 9, 3, 2, 1, "9", 6, 7), 42),
        Pair(listOf("3", 6, 6, 0, "5", 8, 5, "6", 2, "0"), 41)
    )

    @ParameterizedTest
    @MethodSource("testCases")
    fun testFixed(data: Pair<List<Any>, Int>) {
        assertEquals(data.second, sumMixedArray(data.first))
    }
}
