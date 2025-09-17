package org.codewars.kyu8

// https://www.codewars.com/kata/583710ccaa6717322c000105
// Title: Simple multiplication
//
// Description:
// This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
//fun simpleMultiplication(number: Int): Int = number * if (number % 2 == 0) 8 else 9
fun simpleMultiplication(number: Int): Int = number * (8 + number % 2)
