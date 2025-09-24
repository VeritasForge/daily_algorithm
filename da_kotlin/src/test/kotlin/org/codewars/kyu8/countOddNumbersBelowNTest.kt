package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

// https://www.codewars.com/kata/59342039eb450e39970000a6/train/kotlin
// Title: Count Odd Numbers below n
//
// Given a number n, return the number of positive odd numbers below n.
//
// Examples (Input -> Output)
// 7 -> 3 (because 1, 3, 5 are below 7)
// 15 -> 7 (because 1, 3, 5, 7, 9, 11, 13 are below 15)

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class CountOddNumbersBelowNTest {
    @ParameterizedTest(name = "n={0}, expected={1}")
    @MethodSource("testCases")
    fun testOddCount(n: Int, expected: Int) {
        assertEquals(expected, oddCount(n))
    }

    private fun testCases(): Stream<Arguments> = Stream.of(

        Arguments.of(1, 1),
        Arguments.of(2, 1),
        Arguments.of(3, 2),
        Arguments.of(4, 2),
        Arguments.of(5, 3),
        Arguments.of(6, 3),
        Arguments.of(7, 4),
        Arguments.of(15, 7),
        Arguments.of(15023, 7511)
    )
}
