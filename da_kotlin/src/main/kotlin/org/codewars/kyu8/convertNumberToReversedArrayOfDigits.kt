package org.codewars.kyu8

/**
 * [8kyu] Convert number to reversed array of digits
 * https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/kotlin
 *
 * Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
 *
 * Example (Input => Output):
 * 35231 => [1,3,2,5,3]
 * 0     => [0]
 */
fun digitize(n: Long): IntArray {
    return way2(n)
}

fun way1(n: Long): IntArray {
    if (n <= 0) {
        return intArrayOf(0)
    }

    var number = n
    val result = mutableListOf<Int>()

    while (number > 0) {
        result.add((number % 10).toInt())
        number /= 10
    }

    return result.toIntArray()
}

fun way2(n: Long): IntArray = n.toString().reversed().map { it.digitToInt() }.toIntArray()
