package org.exercise

import org.junit.jupiter.api.Test
import org.junit.jupiter.api.Assertions.assertEquals

class CalculatorTest {

    @Test
    fun `덧셈 기능이 올바르게 동작해야 한다`() {
        val expected = 5
        val actual = add(2, 3)
        assertEquals(expected, actual, "2 + 3은 5가 되어야 합니다.")
    }

    @Test
    fun `음수 덧셈 기능도 올바르게 동작해야 한다`() {
        val expected = -1
        val actual = add(-3, 2)
        assertEquals(expected, actual, "-3 + 2는 -1이 되어야 합니다.")
    }
}
