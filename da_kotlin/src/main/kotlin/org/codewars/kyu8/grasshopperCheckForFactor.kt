package org.codewars.kyu8

// https://www.codewars.com/kata/55cbc3586671f6aa070000fb/train/kotlin
// Title: Grasshopper - Check for factor
//
// This function should test if the factor is a factor of base.
//
// Return true if it is a factor or false if it is not.
//
// About factors
// Factors are numbers you can multiply together to get another number.
//
// 2 and 3 are factors of 6 because: 2 * 3 = 6
//
// You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
// For example: 6 % 2 = 0 so 2 is a factor of 6.
// 6 % 3 = 0 so 3 is a factor of 6.
// 6 % 4 = 2 so 4 is not a factor of 6.
//
// Tests
// Factors
// All numbers can be divided by itself.
// 6 % 6 = 0 so 6 is a factor of 6.
// 10 % 10 = 0 so 10 is a factor of 10.
// All numbers can be divided by 1.
// 6 % 1 = 0 so 1 is a factor of 6.
// 10 % 1 = 0 so 1 is a factor of 10.
// All numbers can be divided by negative version of itself.
// 6 % -6 = 0 so -6 is a factor of 6.
// 10 % -10 = 0 so -10 is a factor of 10.
// All numbers can be divided by -1.
// 6 % -1 = 0 so -1 is a factor of 6.
// 10 % -1 = 0 so -1 is a factor of 10.
// Zeros
// 0 is not a factor of any number except 0 itself.
// So 6 % 0 is not a legal operation.
// For the purpose of this kata, you will be tested against numbers greater than 0.
fun checkForFactor(base: Int, factor: Int): Boolean = base % factor == 0
