package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class IsHeGonnaSurviveTest {

    private fun heroTestData() = listOf(
        Arguments.of(10, 5, true),
        Arguments.of(7, 4, false),
        Arguments.of(4, 5, false),
        Arguments.of(100, 40, true),
        Arguments.of(1500, 751, false),
        Arguments.of(0, 1, false)
    )

    @ParameterizedTest
    @MethodSource("heroTestData")
    fun testHero(bullets: Int, dragons: Int, expected: Boolean) {
        assertEquals(expected, hero(bullets, dragons))
    }
}
