
/*
URL: https://www.codewars.com/kata/588417e576933b0ec9000045/train/kotlin
Title: Simple Fun #1: Seats in Theater
Description:
Task
Your friend advised you to see a new performance in the most popular theater in the city. He knows a lot about art and his advice is usually good, but not this time: the performance turned out to be awfully dull. It's so bad you want to leave the theater, which has pretty simple seating arrangement. You decide to calculate the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.

Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're sitting in (row and col), return the number of people who sit strictly behind you and in your column or to the left.

For example, if nCols = 16, nRows = 11, col = 5, and row = 3, the output should be 96.

Input/Output
[input] integer nCols
An integer, the number of theater's columns.
Constraints: 1 ≤ nCols ≤ 1000.
[input] integer nRows
An integer, the number of theater's rows.
Constraints: 1 ≤ nRows ≤ 1000.
[input] integer col
An integer, the column number of your own seat (1-based).
Constraints: 1 ≤ col ≤ nCols.
[input] integer row
An integer, the row number of your own seat (1-based).
Constraints: 1 ≤ row ≤ nRows.
[output] an integer
The number of people who sit strictly behind you and in your column or to the left.
*/
package org.codewars.kyu8

fun seatsInTheater(nCols: Int, nRows: Int, col: Int, row: Int): Int = (nCols - col + 1) * (nRows - row)
