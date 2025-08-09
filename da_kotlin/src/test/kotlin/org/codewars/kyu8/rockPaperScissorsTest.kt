package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class RockPaperScissorsTest {

    private fun testCases() = listOf(
        Arguments.of("Player 1 won!", "rock", "scissors"),
        Arguments.of("Player 1 won!", "scissors", "paper"),
        Arguments.of("Player 1 won!", "paper", "rock"),
        Arguments.of("Player 2 won!", "scissors", "rock"),
        Arguments.of("Player 2 won!", "paper", "scissors"),
        Arguments.of("Player 2 won!", "rock", "paper"),
        Arguments.of("Draw!", "rock", "rock"),
        Arguments.of("Draw!", "scissors", "scissors"),
        Arguments.of("Draw!", "paper", "paper")
    )

    @ParameterizedTest(name = "rps(\"{1}\", \"{2}\") == \"{0}\"")
    @MethodSource("testCases")
    fun testRps(expected: String, p1: String, p2: String) {
        assertEquals(expected, rps(p1, p2))
    }
}
