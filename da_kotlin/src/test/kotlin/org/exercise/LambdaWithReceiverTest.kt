package org.exercise

import org.junit.jupiter.api.Test
import org.junit.jupiter.api.Assertions.assertEquals

class LambdaWithReceiverTest {
    @Test
    fun `수신 객체 지정 람다를 통해 Person 객체를 생성한다 (default parameter 적용)`() {
        // When: 수신 객체 지정 람다인 person 함수를 통해 Person 객체 생성
        val obj: Person = person {}

        // Then: obj의 name과 age는 다음과 같아야 한다.
        assertEquals(obj.name, "default")
        assertEquals(obj.age, -1)
    }

    @Test
    fun `수신 객체 지정 람다를 통해 Person 객체를 생성한다 (age parameter 적용)`() {
        // When: 수신 객체 지정 람다인 person 함수를 통해 Person 객체 생성
        val obj: Person = person { name = "Jay" }

        // Then: obj의 name과 age는 다음과 같아야 한다.
        assertEquals(obj.name, "Jay")
        assertEquals(obj.age, -1)
    }

    @Test
    fun `수신 객체 지정 람다를 통해 Person 객체를 생성한다`() {
        // When: 수신 객체 지정 람다인 person 함수를 통해 Person 객체 생성
        val obj: Person = person {
            name = "Jay"
            age = 30
        }

        // Then: obj의 name과 age는 다음과 같아야 한다.
        assertEquals(obj.name, "Jay")
        assertEquals(obj.age, 30)
    }
}
