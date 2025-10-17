plugins {
    kotlin("jvm") version "2.1.10" // 또는 현재 사용 중인 Kotlin 버전
    application
}

group = "org.example"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(kotlin("test"))

    // Mockk
    testImplementation("io.mockk:mockk:1.14.0")
    // JUnit 5 Jupiter API
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.10.0")
    testImplementation("org.junit.jupiter:junit-jupiter-params:5.10.0")
    // JUnit 5 Jupiter Engine (런타임 시 필요)
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine:5.10.0")

}

tasks.test {
    useJUnitPlatform() // JUnit 5를 사용하도록 설정
}

kotlin {
    jvmToolchain(21) // 또는 현재 사용 중인 JDK 버전
}
