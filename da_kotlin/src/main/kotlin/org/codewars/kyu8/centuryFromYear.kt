package org.codewars.kyu8

import kotlin.div

/**
 * 8 kyu
 * Century From Year
 * https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/kotlin
 *
 * Introduction
 * The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.
 *
 * Task
 * Given a year, return the century it is in.
 *
 * Examples
 * 1705 --> 18
 * 1900 --> 19
 * 1601 --> 17
 * 2000 --> 20
 * 2742 --> 28
 * Note: this kata uses strict construction as shown in the description and the examples, you can read more about it here
 */
fun centuryFromYear(year: Int): Int {
    return way2(year)
}

fun way1(year: Int): Int = (year - 1) / 100 + 1
fun way2(year: Int): Int = (year + 99) / 100
