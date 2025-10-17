/**
 * Kata URL: https://www.codewars.com/kata/554b4ac871d6813a03000035/train/kotlin
 * Title: Highest and Lowest
 *
 * Problem Description:
 * In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
 */
package org.codewars.kyu7

//fun highAndLow(numbers: String): String {
//    val nums = numbers.split(" ").map { it.toInt() }
//    return "${nums.max()} ${nums.min()}"
//}


fun highAndLow(numbers: String): String = numbers.split(" ").map { it.toInt() }.sorted().run {
    "${last()} ${first()}"
}


//fun highAndLow(numbers: String): String = numbers.split(" ").map { it.toInt() }.sorted().let {
//    "${it.last()} ${it.first()}"
//}
