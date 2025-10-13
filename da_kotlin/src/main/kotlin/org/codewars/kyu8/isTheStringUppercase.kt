// https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/kotlin
//
// Kata Title: Is the string uppercase?
//
// Problem Description:
// Create a method `isUpperCase` that checks if all alphabetic characters in a given string are uppercase.
// Non-alphabetic characters should be ignored.
// For example:
// "c" -> false
// "C" -> true
// "hello I AM DONALD" -> false
// "HELLO I AM DONALD" -> true
// "ACSKLDFJSgSKLDFJSKLDFJ" -> false
// "ACSKLDFJSGSKLDFJSKLDFJ" -> true
// "" -> true
// "123" -> true

package org.codewars.kyu8

fun String.isUpperCase(): Boolean = this.none { it.isLowerCase() }
