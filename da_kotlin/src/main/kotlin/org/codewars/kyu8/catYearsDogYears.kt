package org.codewars.kyu8

// https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/kotlin
// Title: Cat Years, Dog Years
//
// I have a cat and a dog.
//
// I got them at the same time as kitten/puppy. That was humanYears years ago.
//
// Return their respective ages now as [humanYears, catYears, dogYears]
//
// NOTES:
//
// humanYears >= 1
// humanYears are whole numbers only
// Cat Years
// 15 cat years for first year
// +9 cat years for second year
// +4 cat years for each year after that
// Dog Years
// 15 dog years for first year
// +9 dog years for second year
// +5 dog years for each year after that

const val FIRST = 15
const val SECOND = 24

fun calculateYears(humanYears: Int): Array<Int> = when (humanYears) {
    1 -> arrayOf(humanYears, FIRST, FIRST)
    2 -> arrayOf(humanYears, SECOND, SECOND)
    else -> {
        val remainYears = (humanYears - 2)
        arrayOf(humanYears,  remainYears * 4 + SECOND, remainYears * 5 + SECOND)
    }
}
