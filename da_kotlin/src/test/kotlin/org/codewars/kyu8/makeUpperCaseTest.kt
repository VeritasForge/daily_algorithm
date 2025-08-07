package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class MakeUpperCaseTest {

    private fun makeUpperCaseDataSource(): List<Arguments> = listOf(
        Arguments.of("hello", "HELLO"),
        Arguments.of("hello world", "HELLO WORLD"),
        Arguments.of("1,2,3", "1,2,3"),
        Arguments.of("!@#$", "!@#$"),
        Arguments.of("abc ABC", "ABC ABC")
    )

    @ParameterizedTest
    @MethodSource("makeUpperCaseDataSource")
    fun `test makeUpperCase`(input: String, expected: String) {
        assertEquals(expected, makeUpperCase(input))
    }
}
