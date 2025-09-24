package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

// https://www.codewars.com/kata/5875b200d520904a04000003/train/kotlin
// Title: Will there be enough space?
//
// The Story:
// Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.
//
// Task Overview:
// You have to write a function that accepts three parameters:
//
// cap is the amount of people the bus can hold excluding the driver.
// on is the number of people on the bus excluding the driver.
// wait is the number of people waiting to get on to the bus excluding the driver.
// If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
//
// Usage Examples:
// cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
// cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class WillThereBeEnoughSpaceTest {
    @ParameterizedTest(name = "cap={0}, on={1}, wait={2} => expected={3}")
    @MethodSource("testCases")
    fun testEnough(cap: Int, on: Int, wait: Int, expected: Int) {
        assertEquals(expected, enough(cap, on, wait))
    }

    private fun testCases(): Stream<Arguments> = Stream.of(
        Arguments.of(10, 5, 5, 0),
        Arguments.of(100, 60, 50, 10),
        Arguments.of(20, 5, 5, 0)
    )
}
