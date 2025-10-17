package org.codewars.kyu7

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class DisemvowelTrollsTest {

    @ParameterizedTest
    @MethodSource("testCases")
    fun disemvowelTest(input: String, expected: String) {
        assertEquals(expected, disemvowel(input))
    }

    private fun testCases(): List<Arguments> {
        return listOf(
            Arguments.arguments("This website is for losers LOL!", "Ths wbst s fr lsrs LL!"),
            Arguments.arguments("No offense but,\nYour writing is among the worst I've ever read", "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"),
            Arguments.arguments("What are you, a communist?", "Wht r y,  cmmnst?")
        )
    }
}
