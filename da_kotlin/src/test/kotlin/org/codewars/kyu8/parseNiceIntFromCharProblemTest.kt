package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

// https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1/train/kotlin
// Title: Parse nice int from char problem
//
// Ask a small girl - "How old are you?". She always says strange things...
//
// She says: "I am 5 years old"
//
// You need to write a function that returns the girl's age (5) as an integer.
//
// Assume the test case input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". The first character in the string is always a number.

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ParseNiceIntFromCharProblemTest {
    @ParameterizedTest(name = "yearsOld={0}, expected={1}")
    @MethodSource("testCases")
    fun testGetAge(yearsOld: String, expected: Int) {
        assertEquals(expected, getAge(yearsOld))
    }

    private fun testCases(): Stream<Arguments> = Stream.of(
        Arguments.of("5 years old", 5),
        Arguments.of("9 years old", 9),
        Arguments.of("1 year old", 1)
    )
}
