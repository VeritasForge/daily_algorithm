package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ConvertABooleanToAStringTest {
    private fun provideTestData() = listOf(
        Arguments.of("true", true),
        Arguments.of("false", false),
    )

    @ParameterizedTest
    @MethodSource("provideTestData")
    fun testConvert(expected: String, input: Boolean) {
        assertEquals(expected, convert(input))
    }
}
