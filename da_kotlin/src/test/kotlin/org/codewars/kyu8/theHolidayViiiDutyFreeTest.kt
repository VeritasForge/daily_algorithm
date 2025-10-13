package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class TheHolidayViiiDutyFreeTest {

    @ParameterizedTest(name = "price={0}, discount={1}, holiday={2} => expected={3}")
    @MethodSource("testCases")
    fun testDutyFree(price: Int, discount: Int, holiday: Int, expected: Int) {
        assertEquals(expected, dutyFree(price, discount, holiday))
    }

    private fun testCases(): List<Arguments> {
        return listOf(
            Arguments.of(12, 50, 1000, 166),
            Arguments.of(17, 10, 500, 294),
            Arguments.of(24, 35, 3000, 357),
            Arguments.of(1400, 35, 10000, 20),
            Arguments.of(700, 20, 10000, 71),
            Arguments.of(377, 40, 9048, 60),
            Arguments.of(2479, 51, 13390, 10),
        )
    }
}
