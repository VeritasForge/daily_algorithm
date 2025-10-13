package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

// https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/kotlin
// Title: Grasshopper - Terminal game move function
//
// In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice two times.
//
// Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.
//
// Example:
// move(3, 6) should be equal to 15

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class GrasshopperTerminalGameMoveFunctionTest {
    @ParameterizedTest(name = "position={0}, roll={1}, expected={2}")
    @MethodSource("testCases")
    fun testMove(position: Int, roll: Int, expected: Int) {
        assertEquals(expected, move(position, roll))
    }

    private fun testCases(): Stream<Arguments> = Stream.of(
        Arguments.of(0, 4, 8),
        Arguments.of(3, 6, 15),
        Arguments.of(2, 5, 12)
    )
}
