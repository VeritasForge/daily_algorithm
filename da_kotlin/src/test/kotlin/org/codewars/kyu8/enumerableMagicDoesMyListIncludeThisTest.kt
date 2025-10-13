
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class EnumerableMagicDoesMyListIncludeThisTest {
    private fun `enumerable magic - does my list include this - test data`(): Stream<Arguments> = Stream.of(
        Arguments.of(listOf(1, 2, 3, 4, 5), 3, true),
        Arguments.of(listOf(1, 2, 3, 4, 5), 6, false),
        Arguments.of(emptyList<Int>(), 1, false)
    )

    @ParameterizedTest
    @MethodSource("enumerable magic - does my list include this - test data")
    fun `test include`(arr: List<Int>, item: Int, expected: Boolean) {
        assertEquals(expected, include(arr, item))
    }
}
