package org.exercise

data class Person(var name: String = "", var age: Int = 0)

/**
 *  Lambda with receiver : 수신 객체 지정 람다
 *  객체 외부의 람다 코드 블록을 마치 해당 객체 내부에서 사용하는 것 처럼 작성할 수 있게 해주는 장치
 */
fun person(name: String = "default", age: Int = -1, block: Person.() -> Unit): Person {
//    // 1. Person 객체를 생성
//    val obj = Person()
//
//    // 2. 생성된 Person 객체(obj)를 수신객체로 감아 파라미터로 받은 람다(block)을 실행
//    obj.block()
//
//    // 3. 람다를 통해 속성이 채워진 Person 객체를 반환
//    return obj

    return Person(name = name, age = age).apply(block)
}
