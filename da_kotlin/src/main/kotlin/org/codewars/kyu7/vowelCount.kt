// https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/kotlin
// Title: Vowel Count
//
// Problem Description:
// Return the number of vowels in the given string.
// We will consider a, e, i, o, u as vowels for this Kata (but not y).
// The input string will only consist of lower case letters and/or spaces.

package org.codewars.kyu7

fun getCount(str: String): Int = str.count { it in "aeiou" }
