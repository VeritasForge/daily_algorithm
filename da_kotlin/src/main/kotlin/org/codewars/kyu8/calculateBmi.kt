package org.codewars.kyu8

fun bmi(weight: Double, height: Double): String {
    val bmiValue = weight / (height * height)
    return when {
        bmiValue <= 18.5 -> "Underweight"
        bmiValue <= 25 -> "Normal"
        bmiValue <= 30 -> "Overweight"
        else -> "Obese"
    }
}
