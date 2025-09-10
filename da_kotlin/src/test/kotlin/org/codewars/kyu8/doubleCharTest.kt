package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class DoubleCharTest {

    private fun doubleCharSamples() = listOf(
        Arguments.of("String", "SSttrriinngg"),
        Arguments.of("Hello World", "HHeelllloo  WWoorrlldd"),
        Arguments.of("1234!_ ", "11223344!!__  "),
        Arguments.of("illuminati", "iilllluummiinnaattii"),
        Arguments.of("1337", "11333377"),
        Arguments.of("!@#$%", "!!@@##$$%%"),
        Arguments.of("", "")
    )

    @ParameterizedTest
    @MethodSource("doubleCharSamples")
    fun `test doubleChar`(s: String, expected: String) {
        assertEquals(expected, doubleChar(s))
    }
}
