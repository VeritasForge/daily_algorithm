/*
URL: https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/kotlin
Title: Sum Mixed Array
Description:
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
Return your answer as a number.
*/

package org.codewars.kyu8

fun sumMixedArray(list: List<Any>): Int = list.sumOf {
    when(it) {
        is Int -> it
        is String -> it.toInt()
        else -> 0
    }
}
