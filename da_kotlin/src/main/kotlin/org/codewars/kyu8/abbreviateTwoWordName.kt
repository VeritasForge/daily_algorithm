package org.codewars.kyu8

/**
 * [8 kyu] Abbreviate a Two Word Name
 * https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/kotlin
 *
 * Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
 *
 * The output should be two capital letters with a dot separating them.
 *
 * It should look like this:
 *
 * Sam Harris => S.H
 *
 * patrick feeney => P.F
 */

//fun abbrevName(name: String): String {
//    return name.split(" ").map{ it.first().uppercase() }.joinToString(".")
//}

fun abbrevName(name: String): String = name.split(" ").joinToString(".") { it.first().uppercase() }
