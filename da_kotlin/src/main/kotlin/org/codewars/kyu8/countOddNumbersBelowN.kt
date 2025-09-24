package org.codewars.kyu8

// https://www.codewars.com/kata/59342039eb450e39970000a6/train/kotlin
// Title: Count Odd Numbers below n
//
// Given a number n, return the number of positive odd numbers below n.
//
// Examples (Input -> Output)
// 7 -> 3 (because 1, 3, 5 are below 7)
// 15 -> 7 (because 1, 3, 5, 7, 9, 11, 13 are below 15)

//fun oddCount(n: Int): Int = (1 .. n - 1).fold(0) { acc, i ->  if (i % 2 != 0) acc + 1 else acc }
fun oddCount(n: Int): Int = n / 2
