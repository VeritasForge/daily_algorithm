
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class ExclamationMarksSeries11ReplaceAllVowelToExclamationMarkInTheSentenceTest {
    private fun testCases(): List<Arguments> = listOf(
        Arguments.of("Hi!", "H!!"),
        Arguments.of("!Hi! Hi!", "!H!! H!!"),
        Arguments.of("aeiou", "!!!!!"),
        Arguments.of("ABCDE", "!BCD!")
    )

    @ParameterizedTest
    @MethodSource("testCases")
    fun `replace all vowel to exclamation mark in the sentence`(s: String, expected: String) {
        assertEquals(expected, replace(s))
    }
}
