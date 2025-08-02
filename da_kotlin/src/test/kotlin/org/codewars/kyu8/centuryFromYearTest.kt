package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class centuryFromYearTest {
    fun methodSource() = listOf (
        Arguments.of(89, 1),
        Arguments.of(1705, 18),
        Arguments.of(1900, 19),
        Arguments.of(1901, 20),
        Arguments.of(2000, 20),
        Arguments.of(2742, 28),
    )

    @ParameterizedTest
    @MethodSource("methodSource")
    fun `century should be returned century number`(number: Int, expected: Int) = assertEquals(expected, centuryFromYear(number))
}
