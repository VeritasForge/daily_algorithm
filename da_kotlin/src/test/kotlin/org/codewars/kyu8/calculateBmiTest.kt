package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class CalculateBmiTest {

    @ParameterizedTest(name = "weight={0}, height={1}, expected={2}")
    @MethodSource("bmiTestCases")
    fun `test bmi calculation`(weight: Double, height: Double, expected: String) {
        assertEquals(expected, bmi(weight, height))
    }

    private fun bmiTestCases(): List<Arguments> {
        return listOf(
            Arguments.of(50.0, 1.80, "Underweight"), // BMI ~15.43
            Arguments.of(70.0, 1.75, "Normal"),      // BMI ~22.86
            Arguments.of(80.0, 1.70, "Overweight"),  // BMI ~27.68
            Arguments.of(100.0, 1.70, "Obese"),      // BMI ~34.60
            Arguments.of(65.0, 1.75, "Normal"),
            Arguments.of(110.0, 1.80, "Obese"),
            Arguments.of(45.0, 1.60, "Underweight")
        )
    }
}
