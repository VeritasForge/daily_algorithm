package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class returningStringsTest {
    fun methodSource() = listOf(
        Arguments.of("Ryan"),
        Arguments.of("Shingles"),
    )

    @ParameterizedTest
    @MethodSource("methodSource")
    fun `greet should be returned proper sentence`(name: String)  = assertEquals("Hello, $name how are you doing today?", greet(name))
}
