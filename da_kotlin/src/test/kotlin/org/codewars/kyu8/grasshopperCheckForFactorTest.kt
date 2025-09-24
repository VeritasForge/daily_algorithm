package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

// https://www.codewars.com/kata/55cbc3586671f6aa070000fb/train/kotlin
// Title: Grasshopper - Check for factor
//
// This function should test if the factor is a factor of base.
//
// Return true if it is a factor or false if it is not.
//
// About factors
// Factors are numbers you can multiply together to get another number.
//
// 2 and 3 are factors of 6 because: 2 * 3 = 6
//
// You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
// For example: 6 % 2 = 0 so 2 is a factor of 6.
// 6 % 3 = 0 so 3 is a factor of 6.
// 6 % 4 = 2 so 4 is not a factor of 6.
//
// Tests
// Factors
// All numbers can be divided by itself.
// 6 % 6 = 0 so 6 is a factor of 6.
// 10 % 10 = 0 so 10 is a factor of 10.
// All numbers can be divided by 1.
// 6 % 1 = 0 so 1 is a factor of 6.
// 10 % 1 = 0 so 1 is a factor of 10.
// All numbers can be divided by negative version of itself.
// 6 % -6 = 0 so -6 is a factor of 6.
// 10 % -10 = 0 so -10 is a factor of 10.
// All numbers can be divided by -1.
// 6 % -1 = 0 so -1 is a factor of 6.
// 10 % -1 = 0 so -1 is a factor of 10.
// Zeros
// 0 is not a factor of any number except 0 itself.
// So 6 % 0 is not a legal operation.
// For the purpose of this kata, you will be tested against numbers greater than 0.
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class GrasshopperCheckForFactorTest {
    @ParameterizedTest(name = "base={0}, factor={1}, expected={2}")
    @MethodSource("testCases")
    fun testCheckForFactor(base: Int, factor: Int, expected: Boolean) {
        assertEquals(expected, checkForFactor(base, factor))
    }

    private fun testCases(): Stream<Arguments> = Stream.of(
        Arguments.of(10, 2, true),
        Arguments.of(63, 7, true),
        Arguments.of(2450, 5, true),
        Arguments.of(24612, 3, true),
        Arguments.of(9, 2, false),
        Arguments.of(653, 7, false),
        Arguments.of(2453, 5, false),
        Arguments.of(24617, 3, false)
    )
}
