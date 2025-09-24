package org.codewars.kyu8

// https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1/train/kotlin
// Title: Parse nice int from char problem
//
// Ask a small girl - "How old are you?". She always says strange things...
//
// She says: "I am 5 years old"
//
// You need to write a function that returns the girl's age (5) as an integer.
//
// Assume the test case input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". The first character in the string is always a number.

//fun getAge(yearsOld: String): Int = yearsOld.first().digitToInt()
fun getAge(yearsOld: String): Int = yearsOld.take(1).toInt()
