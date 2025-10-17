/**
 * Kata URL: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/kotlin
 * Title: List Filtering
 *
 * Problem Description:
 * In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
 */
package org.codewars.kyu7

//fun filterList(l: List<Any>): List<Int> = l.filter { it is Int && it.toInt() > -1 }.map { it.toString().toInt() }
fun filterList(l: List<Any>): List<Int> = l.filterIsInstance<Int>()
