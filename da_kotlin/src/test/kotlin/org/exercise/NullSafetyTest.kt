package org.exercise

import org.junit.jupiter.api.Test
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertNull
import org.junit.jupiter.api.Assertions.assertThrows
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource


@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class NullSafetyTest {

    fun safeCallOperatorSource() = listOf(
        Arguments.of("Jay", "Jay".length),
        Arguments.of(null, null)
    )

    @ParameterizedTest
    @MethodSource("safeCallOperatorSource")
    fun `안전 호출 연산자(Safe Call Operator)`(name: String?, expectedLength: Int?) {
        // Given
        val personName: String? = name

        // When: name이 null이면 length를 호출하지 않고 null을 반환 (vise versa)
        val result = personName?.length

        // Then
        assertEquals(result, expectedLength)
    }

    fun elvisOperatorSource() = listOf(
        Arguments.of("Jay", "Jay".length),
        Arguments.of(null, 0)
    )

    @ParameterizedTest
    @MethodSource("elvisOperatorSource")
    fun `엘비스 연산자 (Elvis Operator)`(name: String?, expectedLength: Int?) {
        // Given
        val personName: String? = name

        // When: name이 null이면 0을 반환하고, name이 null이 아니면 length를 호출
        val result = personName?.length ?: 0

        // Then
        assertEquals(result, expectedLength)
    }

    @Test
    fun `Non-null Assertion`() {
        // Given
        val name: String? = null

        // When: Non-null Assertion 사용 시!!
        // Then: NPE이 발생해야 한다.
        assertThrows(NullPointerException::class.java) { name!!.length}
    }

    @Test
    fun `강제 타입 변환(Unsafe Case)`() {
        // Given
        val someValue: Any = 123

        // When: someValue는 Int이므로 String으로 변환 불가. 따라서 강제 타입 변환을 하면,
        // Then: ClassCastException 발생!
        assertThrows(ClassCastException::class.java) { someValue as String }
    }

    @Test
    fun `안전 타입 변환(Safe Case)`() {
        // Given
        val someValue: Any = 123

        // When: someValue는 Int이므로 String으로 변환 불가. 하지만 안전 타입 변환을 하면,
        // Then: null을 반환
        assertNull(someValue as? String)
    }
}
