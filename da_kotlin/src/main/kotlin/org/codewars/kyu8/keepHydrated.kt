package org.codewars.kyu8

/**
 * [8kyu] Keep Hydrated!
 * https://www.codewars.com/kata/582cb0224e56e068d800003c/train/kotlin
 *
 * Nathan loves cycling.
 *
 * Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
 *
 * You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.
 *
 * For example:
 *   time = 3 ----> litres = 1
 *   time = 6.7---> litres = 3
 *   time = 11.8--> litres = 5
 */
fun litres(time: Double): Int = (time * 0.5).toInt()
