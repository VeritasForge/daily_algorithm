package org.codewars.kyu8

// https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/solutions/kotlin
//fun invert(arr: IntArray): IntArray = arr.map { -it }.toIntArray()
fun invert(arr: IntArray) = IntArray(arr.size) { -arr[it] }
