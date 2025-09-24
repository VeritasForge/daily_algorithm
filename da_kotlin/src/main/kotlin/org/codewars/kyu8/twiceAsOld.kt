package org.codewars.kyu8

import kotlin.math.abs

// https://www.codewars.com/kata/5b853229cfde412a470000d0/train/kotlin
// Title: Twice as old
//
// Your function takes two arguments:
//
// current father's age (years)
// current age of his son (years)
// Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).

fun twiceAsOld(dadYearsOld: Int, sonYearsOld: Int): Int = abs(dadYearsOld - (sonYearsOld * 2))
