package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class IfYouCantSleepJustCountSheepTest {

    private fun testCases() = listOf(
        Arguments.of("", 0),
        Arguments.of("1 sheep...", 1),
        Arguments.of("1 sheep...2 sheep...", 2),
        Arguments.of("1 sheep...2 sheep...3 sheep...", 3)
    )

    @ParameterizedTest(name = "countSheep({1}) == \"{0}\"")
    @MethodSource("testCases")
    fun testCountSheep(expected: String, num: Int) {
        assertEquals(expected, countSheep(num))
    }
}
