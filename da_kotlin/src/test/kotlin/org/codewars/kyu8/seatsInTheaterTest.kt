
package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class SeatsInTheaterTest {

    private fun seatsInTheaterTestCases() = listOf(
        Arguments.of(16, 11, 5, 3, 96),
        Arguments.of(1, 1, 1, 1, 0),
        Arguments.of(13, 6, 8, 3, 18),
        Arguments.of(60, 100, 60, 1, 99),
        Arguments.of(1000, 1000, 1000, 1000, 0)
    )

    @ParameterizedTest
    @MethodSource("seatsInTheaterTestCases")
    fun `test seatsInTheater`(nCols: Int, nRows: Int, col: Int, row: Int, expected: Int) {
        assertEquals(expected, seatsInTheater(nCols, nRows, col, row))
    }
}
