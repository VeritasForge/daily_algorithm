package org.codewars.kyu8

// Clock shows h hours, m minutes, s seconds after midnight.
// Your task is to write a function which returns the time since midnight in milliseconds.
//fun past(h: Int, m: Int, s: Int): Int = h * 3_600_000 + m * 60_000 + s * 1_000
fun past(h: Int, m: Int, s: Int): Int = ((h * 60 + m) * 60 + s) * 1_000
