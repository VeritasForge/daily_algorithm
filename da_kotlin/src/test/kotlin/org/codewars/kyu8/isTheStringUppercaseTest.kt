package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class IsTheStringUppercaseTest {

    @ParameterizedTest(name = "String: \"{0}\", Expected: {1}")
    @MethodSource("testCases")
    fun `test isUpperCase`(input: String, expected: Boolean) {
        assertEquals(expected, input.isUpperCase())
    }

    private fun testCases() = listOf(
        Arguments.of("c", false),
        Arguments.of("C", true),
        Arguments.of("hello I AM DONALD", false),
        Arguments.of("HELLO I AM DONALD", true),
        Arguments.of("ACSKLDFJSgSKLDFJSKLDFJ", false),
        Arguments.of("ACSKLDFJSGSKLDFJSKLDFJ", true),
        Arguments.of("", true),
        Arguments.of("123", true),
        Arguments.of("a", false),
        Arguments.of("A", true),
        Arguments.of("Hello", false),
        Arguments.of("HELLO WORLD", true),
        Arguments.of("HELLO WORLD!", true)
    )
}
