package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class AbbreviateTwoWordNameTest {

    fun methodSource() = listOf(
        Arguments.of("Sam Harris", "S.H"),
        Arguments.of("patrick feeney", "P.F"),
    )

    @ParameterizedTest
    @MethodSource("methodSource")
    fun `abbreviate a two word name`(name: String, expected: String) {
        // When:
        val actual = abbrevName(name)

        // Then:
        assertEquals(actual, expected)
    }
}
