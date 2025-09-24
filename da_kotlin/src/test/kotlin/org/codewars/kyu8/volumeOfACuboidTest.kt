package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

// https://www.codewars.com/kata/58261acb22be6e2ed800003a/train/kotlin
// Title: Volume of a Cuboid
//
// Bob needs a fast way to calculate the volume of a cuboid with three values: the length, width and height of the cuboid. Write a function to help Bob with this calculation.

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class VolumeOfACuboidTest {
    @ParameterizedTest(name = "length={0}, width={1}, height={2}, expected={3}")
    @MethodSource("testCases")
    fun testGetVolumeOfCuboid(length: Double, width: Double, height: Double, expected: Double) {
        assertEquals(expected, getVolumeOfCuboid(length, width, height), 0.0001)
    }

    private fun testCases(): Stream<Arguments> = Stream.of(
        Arguments.of(1.0, 2.0, 2.0, 4.0),
        Arguments.of(6.3, 2.0, 5.0, 63.0)
    )
}
