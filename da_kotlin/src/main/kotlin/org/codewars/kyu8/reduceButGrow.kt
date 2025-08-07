package org.codewars.kyu8

// https://www.codewars.com/kata/57f780909f7e8e3183000078/train/kotlin
//fun grow(arr: IntArray): Int = arr.reduce { acc, num -> acc * num }
fun grow(arr: IntArray): Int = arr.reduce(Int::times)
