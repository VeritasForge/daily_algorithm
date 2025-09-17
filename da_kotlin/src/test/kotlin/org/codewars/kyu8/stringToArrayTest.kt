package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class StringToArrayTest {

    private fun testCases() = listOf(
        Arguments.of("Robin Singh", listOf("Robin", "Singh")),
        Arguments.of("CodeWars", listOf("CodeWars")),
        Arguments.of("I love arrays they are my favorite", listOf("I", "love", "arrays", "they", "are", "my", "favorite")),
        Arguments.of("1 2 3", listOf("1", "2", "3")),
        Arguments.of("", listOf(""))
    )

    @ParameterizedTest
    @MethodSource("testCases")
    fun `should convert string to array of words`(input: String, expected: List<String>) {
        assertEquals(expected, stringToArray(input))
    }
}
