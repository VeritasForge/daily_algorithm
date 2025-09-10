package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class TheFeastOfManyBeastsTest {

    private fun feastSamples() = listOf(
        Arguments.of("great blue heron", "garlic naan", true),
        Arguments.of("chickadee", "chocolate cake", true),
        Arguments.of("brown bear", "bear claw", false),
        Arguments.of("marmot", "mulberry tart", true),
        Arguments.of("lion", "lasagna", false),
        Arguments.of("electric eel", "lasagna", false),
        Arguments.of("cat", "bat", false)
    )

    @ParameterizedTest
    @MethodSource("feastSamples")
    fun `test feast`(beast: String, dish: String, expected: Boolean) {
        assertEquals(expected, feast(beast, dish))
    }
}
