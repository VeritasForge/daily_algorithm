package org.codewars.kyu8

import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test

class UpAndDownTheStringGrowsTest {

    @Test
    fun `strange string should grow in size after uppercase and lowercase`() {
        assertTrue(
            STRANGE_STRING.uppercase().lowercase().length > STRANGE_STRING.length,
            "The size of STRANGE_STRING should be greater after uppercase and then lowercase transformations."
        )
    }
}
