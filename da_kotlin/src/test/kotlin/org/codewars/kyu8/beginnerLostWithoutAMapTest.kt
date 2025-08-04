package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertArrayEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class BeginnerLostWithoutAMapTest {
    fun provideTestData(): Stream<Arguments> {
        return Stream.of(
            Arguments.of(intArrayOf(2, 4, 6), intArrayOf(1, 2, 3)),
            Arguments.of(intArrayOf(8, 2, 2, 2, 8), intArrayOf(4, 1, 1, 1, 4)),
            Arguments.of(intArrayOf(4, 4, 4, 4, 4, 4), intArrayOf(2, 2, 2, 2, 2, 2))
        )
    }

    @ParameterizedTest
    @MethodSource("provideTestData")
    fun testMaps(expected: IntArray, input: IntArray) {
        assertArrayEquals(expected, maps(input))
    }
}
