package org.codewars.kyu8

/*
URL: https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/kotlin

Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:
rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!
*/

fun rps(p1: String, p2: String): String {
    if (p1 == p2) return "Draw!"

    return when (p1 to p2) {
        "rock" to "scissors",
        "scissors" to "paper",
        "paper" to "rock" -> "Player 1 won!"
        else -> "Player 2 won!"
    }
}
