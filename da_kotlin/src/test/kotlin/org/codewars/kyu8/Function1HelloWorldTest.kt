package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class Function1HelloWorldTest {
    @Test
    fun `greet should return 'hello world!'`() {
        assertEquals("hello world!", greet())
    }
}
