package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class TotalAmountOfPointsTest {

    private fun testCases() = listOf(
        Arguments.of(30, listOf("1:0","2:0","3:0","4:0","2:1","3:1","4:1","3:2","4:2","4:3")),
        Arguments.of(10, listOf("1:1","2:2","3:3","4:4","2:2","3:3","4:4","3:3","4:4","4:4")),
        Arguments.of(0, listOf("0:1","0:2","0:3","0:4","1:2","1:3","1:4","2:3","2:4","3:4")),
        Arguments.of(12, listOf("1:0","2:0","3:0","4:4","2:2","3:3","1:4","2:3","2:4","3:4")),
        Arguments.of(15, listOf("1:0","2:0","3:0","4:0","2:1","1:3","1:4","2:3","2:4","3:4"))
    )

    @ParameterizedTest
    @MethodSource("testCases")
    fun testPoints(expected: Int, games: List<String>) {
        assertEquals(expected, points(games))
    }
}
