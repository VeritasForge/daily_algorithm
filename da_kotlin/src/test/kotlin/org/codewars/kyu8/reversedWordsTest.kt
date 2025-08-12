package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ReversedWordsTest {

    private fun testCases() = listOf(
        Arguments.of("world! hello", "hello world!"),
        Arguments.of("yoda doesn't speak like this", "this like speak doesn't yoda"),
        Arguments.of("foobar", "foobar"),
        Arguments.of("kata editor", "editor kata"),
        Arguments.of("row row row your boat", "boat your row row row")
    )

    @ParameterizedTest(name = "reverseWords(\"{1}\") == \"{0}\"")
    @MethodSource("testCases")
    fun testReverseWords(expected: String, input: String) {
        assertEquals(expected, reverseWords(input))
    }
}
