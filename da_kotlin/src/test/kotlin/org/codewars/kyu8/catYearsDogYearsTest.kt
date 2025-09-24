package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertArrayEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

// https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/kotlin
// Title: Cat Years, Dog Years
//
// I have a cat and a dog.
//
// I got them at the same time as kitten/puppy. That was humanYears years ago.
//
// Return their respective ages now as [humanYears, catYears, dogYears]
//
// NOTES:
//
// humanYears >= 1
// humanYears are whole numbers only
// Cat Years
// 15 cat years for first year
// +9 cat years for second year
// +4 cat years for each year after that
// Dog Years
// 15 dog years for first year
// +9 dog years for second year
// +5 dog years for each year after that

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class CatYearsDogYearsTest {

    @ParameterizedTest(name = "humanYears: {0}, expected: {1}")
    @MethodSource("data")
    fun testCalculateYears(humanYears: Int, expected: Array<Int>) {
        assertArrayEquals(expected, calculateYears(humanYears))
    }

    private fun data(): Stream<Arguments> = Stream.of(
        Arguments.of(1, arrayOf(1, 15, 15)),
        Arguments.of(2, arrayOf(2, 24, 24)),
        Arguments.of(10, arrayOf(10, 56, 64))
    )
}
