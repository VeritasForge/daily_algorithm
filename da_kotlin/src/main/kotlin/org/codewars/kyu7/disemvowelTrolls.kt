/**
 * Kata URL: https://www.codewars.com/kata/52fba66badcd10859f00097e/train/kotlin
 * Title: Disemvowel Trolls
 *
 * Problem Description:
 * Trolls are attacking your comment section!
 * A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
 * Your task is to write a function that takes a string and return a new string with all vowels removed.
 * For this kata 'y' isn't considered a vowel.
 */
package org.codewars.kyu7

fun disemvowel(str: String): String = str.replace(Regex("[aeiou]", RegexOption.IGNORE_CASE), "")
