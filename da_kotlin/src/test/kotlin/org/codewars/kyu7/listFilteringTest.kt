package org.codewars.kyu7

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ListFilteringTest {

    @ParameterizedTest(name = "Input: {0}, Expected: {1}")
    @MethodSource("testCases")
    fun `test list filtering`(input: List<Any>, expected: List<Int>) {
        assertEquals(expected, filterList(input))
    }

    private fun testCases(): List<Arguments> {
        return listOf(
            Arguments.of(listOf(1, 2, "a", "b"), listOf(1, 2)),
            Arguments.of(listOf(1, "a", "b", 0, 15), listOf(1, 0, 15)),
            Arguments.of(listOf(1, 2, "aasf", "1", "123", 123), listOf(1, 2, 123)),
            Arguments.of(emptyList<Any>(), emptyList<Int>())
        )
    }
}
