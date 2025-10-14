package org.codewars.kyu7

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class VowelCountTest {
    @ParameterizedTest(name = "getCount(\"{0}\") should be {1}")
    @MethodSource("testCases")
    fun testGetCount(str: String, expected: Int) {
        assertEquals(expected, getCount(str))
    }

    private fun testCases() = listOf(
        Arguments.of("abracadabra", 5),
        Arguments.of("test", 1),
        Arguments.of("", 0),
        Arguments.of("aeiou", 5),
        Arguments.of("bcdfghjklmnpqrstvwxyz", 0),
        Arguments.of("my pyx", 0)
    )
}
