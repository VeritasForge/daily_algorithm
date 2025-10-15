// URL: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/go
// Title: Even or Odd
// Description: Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
package kyu8

func EvenOrOdd(number int) string {
	return []string{"Even", "Odd"}[number&1]
}
