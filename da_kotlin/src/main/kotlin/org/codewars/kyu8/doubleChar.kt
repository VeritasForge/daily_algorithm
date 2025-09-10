/*
* Kata: Double Char (8 kyu)
* URL: https://www.codewars.com/kata/56b1f01c247c01db92000076
*
* Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
*
* For example:
* * "String"      -> "SSttrriinngg"
* * "Hello World" -> "HHeelllloo  WWoorrlldd"
* * "1234!_ "     -> "11223344!!__  "
*/

package org.codewars.kyu8

fun doubleChar(s: String): String = s.map { "$it$it" }.joinToString("")
