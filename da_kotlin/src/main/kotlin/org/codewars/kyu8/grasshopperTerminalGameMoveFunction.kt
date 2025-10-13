package org.codewars.kyu8

// https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/kotlin
// Title: Grasshopper - Terminal game move function
//
// In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice two times.
//
// Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.
//
// Example:
// move(3, 6) should be equal to 15

fun move(position: Int, roll: Int): Int = position + roll * 2
