package org.codewars.kyu8

/**
 * [8kyu] Reversed sequence
 * https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/kotlin
 *
 * Build a function that returns an array of integers from n to 1 where n>0.
 * Example : n=5 --> [5,4,3,2,1]
 *
 */
//fun reversedSequence(n: Int): List<Int> = (n downTo 1).toList()
//fun reversedSequence(n: Int): List<Int> = n.downTo(1) .toList()
fun reversedSequence(n: Int): List<Int> = List(n) { n - it }
