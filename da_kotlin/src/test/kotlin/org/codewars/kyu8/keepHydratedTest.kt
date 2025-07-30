package org.codewars.kyu8

import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource


@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class keepHydratedTest {
    fun methodSource() = listOf(
        Arguments.of(3, 1),
        Arguments.of(6.7, 3),
        Arguments.of(11.8, 5),
    )

    @ParameterizedTest
    @MethodSource("methodSource")
    fun `keep hydrated`(time: Double, expected: Int) {
        // When:
        val actual = litres(time)

        // Then:
        assertEquals(actual, expected)

    }
}
