package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ClosestElevatorTest {

    @ParameterizedTest(name = "left={0}, right={1}, call={2} => {3}")
    @MethodSource("testCases")
    fun testClosestElevator(left: Int, right: Int, call: Int, expected: String) {
        assertEquals(expected, elevator(left, right, call))
    }

    private fun testCases() = listOf(
        arrayOf(0, 1, 0, "left"),
        arrayOf(0, 1, 1, "right"),
        arrayOf(0, 1, 2, "right"),
        arrayOf(0, 0, 0, "right"),
        arrayOf(0, 2, 1, "right")
    )
}
