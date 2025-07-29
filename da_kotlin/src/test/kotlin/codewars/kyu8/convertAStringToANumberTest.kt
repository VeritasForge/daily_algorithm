package org.example.org.codewars.kyu8

import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ConvertStringToNumberTest {

    fun convertStringToNumberSample() = listOf(
        Arguments.of("1234", 1234),
        Arguments.of("605", 605),
        Arguments.of("1405", 1405),
        Arguments.of("-7", -7),
    )

    @ParameterizedTest
    @MethodSource("convertStringToNumberSample")
    fun `convert a string to a number`(str: String, expected: Int) {
        // When:
        val actual = stringToNumber(str)

        // Then:
        assertEquals(actual, expected)
    }
}
