package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class WellOfIdeasEasyVersionTest {

    private fun testCases(): List<Arguments> = listOf(
        Arguments.of(arrayOf("bad", "bad", "bad"), "Fail!"),
        Arguments.of(arrayOf("good", "bad", "bad", "bad", "bad"), "Publish!"),
        Arguments.of(arrayOf("good", "bad", "bad", "bad", "bad", "good", "bad", "bad", "good"), "I smell a series!")
    )

    @ParameterizedTest
    @MethodSource("testCases")
    fun `test well of ideas`(x: Array<String>, expected: String) {
        assertEquals(expected, well(x))
    }
}
