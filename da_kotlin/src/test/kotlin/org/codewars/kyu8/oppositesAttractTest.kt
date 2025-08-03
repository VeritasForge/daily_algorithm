package org.codewars.kyu8

import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class oppositesAttractTest {

    fun methodSource() = listOf(
        Arguments.of(1, 4, true),
        Arguments.of(2, 2, false),
        Arguments.of(0, 1, true),
        Arguments.of(0, 0, false),
    )

    @ParameterizedTest
    @MethodSource("methodSource")
    fun test(a: Int, b: Int, expected: Boolean) = assertEquals(expected, loveFun(a, b))
}
