package org.codewars.kyu8

// https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/kotlin
//fun countPositivesSumNegatives(input : Array<Int>?) : Array<Int>  {
//    if (input.isNullOrEmpty()) return emptyArray()
//
//    val positiveCount = input.count{ it > 0 }
//    val negativeSum = input.filter{ it < 0 }.sum()
//
//    return arrayOf(positiveCount, negativeSum)
//}

fun countPositivesSumNegatives(input : Array<Int>?) : Array<Int> {
    if (input.isNullOrEmpty()) return emptyArray()
    val (positives, negatives) = input.partition { it > 0 }
    return arrayOf(positives.count(), negatives.sum())
}
