package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class AreaOrPerimeterTest {

    private fun basicTests() = listOf(
        Arguments.of(3, 3, 9),
        Arguments.of(6, 10, 32)
    )

    @ParameterizedTest
    @MethodSource("basicTests")
    fun test(l: Int, w: Int, expected: Int) {
        assertEquals(expected, areaOrPerimeter(l, w))
    }
}
