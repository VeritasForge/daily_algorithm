package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

// https://www.codewars.com/kata/5b853229cfde412a470000d0/train/kotlin
// Title: Twice as old
//
// Your function takes two arguments:
//
// current father's age (years)
// current age of his son (years)
// Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class TwiceAsOldTest {
    @ParameterizedTest(name = "dadYearsOld={0}, sonYearsOld={1}, expected={2}")
    @MethodSource("testCases")
    fun testTwiceAsOld(dadYearsOld: Int, sonYearsOld: Int, expected: Int) {
        assertEquals(expected, twiceAsOld(dadYearsOld, sonYearsOld))
    }

    private fun testCases(): Stream<Arguments> = Stream.of(
        Arguments.of(36, 7, 22),
        Arguments.of(55, 30, 5),
        Arguments.of(42, 21, 0),
        Arguments.of(22, 1, 20),
        Arguments.of(29, 0, 29)
    )
}
