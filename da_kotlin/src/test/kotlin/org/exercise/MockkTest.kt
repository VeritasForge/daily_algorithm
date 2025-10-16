package org.exercise

import io.mockk.every
import io.mockk.just
import io.mockk.mockk
import io.mockk.mockkConstructor
import io.mockk.mockkObject
import io.mockk.mockkStatic
import io.mockk.runs
import io.mockk.slot
import io.mockk.spyk
import io.mockk.unmockkConstructor
import io.mockk.unmockkObject
import io.mockk.unmockkStatic
import io.mockk.verify
import io.mockk.verifyOrder
import io.mockk.verifySequence
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test

// 테스트 대상 클래스
class Calculator(private val adder: Adder) {
    fun add(a: Int, b: Int): Int {
        return adder.add(a, b)
    }
}

// 의존성 인터페이스
interface Adder {
    fun add(a: Int, b: Int): Int
}

interface MultiFunctionService {
    fun performActionA(): String
    fun performActionB(): Int
    fun logEvent() // Unit 반환
}

class DataProcessor {
    fun fetchData(): String {
        // 실제로는 데이터베이스나 네트워크에서 데이터를 가져오는 복잡한 로직
        println("Fetching real data...")
        return "Real Data"
    }

    fun process(): String {
        val data = fetchData()
        return "Processed: $data"
    }
}

class DataManager {
    fun fetchData(onSuccess: (String) -> Unit, onError: (Exception) -> Unit) {
        try {
            // 네트워크 통신 시뮬레이션
            val data = "데이터"
            onSuccess(data)
        } catch (e: Exception) {
            onError(e)
        }
    }
}

object AnalyticsService {
    fun trackEvent(eventName: String) {
        // 실제로는 원격 서버로 이벤트를 전송
        println("Tracking event: $eventName")
    }
}

class EventProcessor(private val analytics: AnalyticsService = AnalyticsService) {
    fun processLoginEvent() {
        analytics.trackEvent("login_success")
    }
}

fun getCurrentTimestamp(): Long = System.currentTimeMillis()

fun getName(): String = "test"

// String 클래스에 대한 확장 함수
fun String.ellipsize(maxLength: Int): String {
    return if (this.length > maxLength) this.substring(0, maxLength) + "..." else this
}


class Dependency {
    fun doWork(): String = "Real Work"
}

class ServiceWithHardcodedDependency {
    fun execute(): String {
        val dependency = Dependency() // 의존성을 직접 생성 (테스트하기 어려움)
        return dependency.doWork()
    }
}


class MockkTest {
    @Test
    fun `계산기는 Adder를 사용하여 두 숫자를 더해야 한다`() {
        // 준비(Arrange): Adder 인터페이스의 모의 객체를 생성한다.
        val mockAdder = mockk<Adder>()
        val calculator = Calculator(mockAdder)

        //... 실행 및 검증 단계
        // mockAdder.add(2, 3) 호출이 발생하면 5를 반환하도록 정의한다.
        every { mockAdder.add(2, 3) } returns 5

        // 실행(Act)
        val result = calculator.add(2, 3)

        // 검증(Assert)
        assertEquals(5, result)
    }

    @Test
    fun `process 메서드는 fetchData의 결과를 가공해야 한다`() {
        // 준비(Arrange): 실제 DataProcessor 객체를 생성하고 spyk로 감싼다.
        val realProcessor = DataProcessor()
        val spyProcessor = spyk(realProcessor)

        // spyProcessor의 fetchData 메서드만 가짜 동작으로 대체한다.
        every { spyProcessor.fetchData() } returns "Mocked Data"

        // 실행(Act): process 메서드를 호출한다.
        // 이 때 내부에서 호출되는 fetchData()는 위에서 정의한 대로 "Mocked Data"를 반환한다.
        // process() 메서드 자체의 로직은 실제 객체의 것을 그대로 따른다.
        val result = spyProcessor.process()

        // 검증(Assert)
        assertEquals("Processed: Mocked Data", result)

        // fetchData가 호출되었는지 검증한다.
        verify { spyProcessor.fetchData() }
    }

    @Test
    fun `ActionA의 결과만 테스트하고 싶을 때`() {
        // 준비(Arrange): relaxed mock을 생성한다.
        val relaxedMock = mockk<MultiFunctionService>(relaxed = true)

        // performActionA에 대한 행위만 정의한다.
        every { relaxedMock.performActionA() } returns "Action A Complete"

        // 실행(Act)
        val resultA = relaxedMock.performActionA()
        val resultB = relaxedMock.performActionB() // 스터빙되지 않았지만 예외가 발생하지 않음
        relaxedMock.logEvent() // 스터빙되지 않았지만 예외가 발생하지 않음

        // 검증(Assert)
        assertEquals("Action A Complete", resultA)
        assertEquals(0, resultB) // Int의 기본값 0이 반환됨
        verify { relaxedMock.logEvent() } // 호출 검증은 정상적으로 동작함
    }

    @Test
    fun `로그인 이벤트가 처리될 때 trackEvent가 호출되어야 한다`() {
        // 준비(Arrange): AnalyticsService 객체를 모킹한다.
        mockkObject(AnalyticsService)
        every { AnalyticsService.trackEvent(any()) } just runs

        // 실행(Act)
        val processor = EventProcessor()
        processor.processLoginEvent()

        // 검증(Assert)
        verify { AnalyticsService.trackEvent("login_success") }

        // 중요: 테스트가 끝난 후 모킹을 해제하여 다른 테스트에 영향을 주지 않도록 한다.
        //      당연히 @AfterEach 에서 처리되어야 하지만, 공부하는거니 간단히 이렇게 처리
        unmockkObject(AnalyticsService)
    }

    @Test
    fun `고정된 타임스탬프를 반환하도록 모킹하기`() {
        // 준비(Arrange): 최상위 함수를 모킹한다.
        //  mockkStatic("org.exercise.MockkTestKt")를 호출하는 것은 해당 파일의 최상위
        //  함수들을 "모킹할 수 있도록 준비"하는 단계라고 생각하시면 됩니다.
        //
        //  더 자세히 설명해 드릴게요.
        //
        //   1. `mockkStatic`의 역할:
        //       * mockkStatic은 지정된 클래스(이 경우, MockkTest.kt 파일의 최상위 함수들을
        //         담고 있는 MockkTestKt 클래스)의 정적 메서드들을 MockK의 통제 하에 둡니다.
        //       * 이것은 마치 해당 함수들을 조작할 수 있는 '리모컨'을 얻는 것과 같습니다.
        //         리모컨을 얻었다고 해서 TV 채널이 저절로 바뀌지는 않는 것과 같죠.
        //
        //   2. `every`의 역할:
        //       * mockkStatic으로 모킹 준비가 된 함수들 중에서, 실제로 동작을 변경하고 싶은
        //         함수를 every 블록을 사용해 지정해야 합니다.
        //       * every { getCurrentTimestamp() } returns 12345L 처럼 every를 사용해야
        //         비로소 getCurrentTimestamp 함수의 실제 구현 대신 정의된 12345L을 반환하게
        //         됩니다.
        //
        //   3. 스터빙하지 않은 함수의 동작:
        //       * mockkStatic으로 파일을 지정했더라도, every로 따로 동작을 정의하지 않은
        //         다른 최상위 함수들은 원래의 실제 구현대로 동작합니다.
        //
        //  요약:
        //
        //  mockkStatic은 "이제부터 이 파일에 있는 최상위 함수들을 내가 관리할게. 어떤
        //  함수를 어떻게 바꿀지는 every로 알려줘" 라고 선언하는 것과 같습니다. 따라서
        //  mockkStatic 호출만으로는 아무것도 바뀌지 않으며, every를 통해 원하는 함수만
        //  골라서 모킹(스터빙)할 수 있습니다.
        mockkStatic("org.exercise.MockkTestKt")
        every { getCurrentTimestamp() } returns 12345L

        // 실행 및 검증
        assertEquals(12345L, getCurrentTimestamp())
        assertEquals("test", getName())

        unmockkStatic("org.exercise.MockkTestKt")
    }

    @Test
    fun `확장 함수 모킹하기`() {
        // 준비(Arrange): String 클래스의 확장 함수를 모킹한다.
        mockkStatic(String::ellipsize)
        val testString = "This is a very long string"
        every { testString.ellipsize(10) } returns "shortened"

        // 실행 및 검증
        assertEquals("shortened", testString.ellipsize(10))

        unmockkStatic(String::ellipsize)
    }

    @Test
    fun `하드코딩된 의존성의 생성자를 모킹하기`() {
        // 준비(Arrange): Dependency 클래스의 생성자를 모킹한다.
        mockkConstructor(Dependency::class)

        // 생성자를 통해 만들어질 모의 객체의 행위를 정의한다.
        // anyConstructed<T>()를 사용하여 해당 모의 객체를 참조한다.
        every { anyConstructed<Dependency>().doWork() } returns "Mocked Work"

        // 실행(Act)
        val service = ServiceWithHardcodedDependency()
        val result = service.execute()

        // 검증(Assert)
        assertEquals("Mocked Work", result)
        verify { anyConstructed<Dependency>().doWork() }

        unmockkConstructor(Dependency::class)
    }

    @Test
    fun `호출 횟수 검증하기`() {
        // relaxUnitFun은 함수의 반환 타입이 'Unit'인 함수들에 대해서만 'relaxed' 모드를 적용
//        val mockList = mockk<MutableList<String>>(relaxUnitFun = true)
        val mockList = mockk<MutableList<String>>(relaxed = true)

        mockList.add("one")
        mockList.add("two")
        mockList.add("two")

        // "two"가 정확히 2번 추가되었는지 검증
        verify(exactly = 2) { mockList.add("two") }

        // add(any())가 최소 3번 이상 호출되었는지 검증
        verify(atLeast = 3) { mockList.add(any()) }

        // clear() 메서드는 호출되지 않았음을 검증
        verify(exactly = 0) { mockList.clear() }
    }

    @Test
    fun `호출 순서 검증`() {
        val mockA = mockk<Runnable>(relaxUnitFun = true)
        val mockB = mockk<Runnable>(relaxUnitFun = true)

        mockA.run()
        mockB.run()
        mockA.run()

        // mockA.run()이 mockB.run()보다 먼저 호출되었는지 검증 (성공)
        verifyOrder {
            mockA.run()
            mockB.run()
        }

        // mockA.run() -> mockB.run() -> mockA.run() 순서로 정확히 호출되었는지 검증 (성공)
        verifySequence {
            mockA.run()
            mockB.run()
            mockA.run()
        }
    }

    @Test
    fun `데이터 로딩 성공 시 콜백이 올바른 데이터와 함께 호출되는지 검증 (행위 기반 테스트)`() {
        // [패턴 B: 행위 기반 테스트]
        // 준비(Arrange)
        val manager = DataManager() // 실제 객체를 그대로 사용
        val mockOnSuccess = mockk<(String) -> Unit>(relaxed = true) // 콜백 함수 자체를 모의 객체로 생성

        // 실행(Act)
        manager.fetchData(
            onSuccess = mockOnSuccess,
            onError = { /* no-op */ }
        )

        // 검증(Assert)
        // mockOnSuccess 콜백이 "성공 데이터"라는 인자와 함께
        // 정확히 1번 '호출'되었는지 '행위'를 직접 검증
        verify(exactly = 1) { mockOnSuccess.invoke("성공 데이터") }
    }
}
