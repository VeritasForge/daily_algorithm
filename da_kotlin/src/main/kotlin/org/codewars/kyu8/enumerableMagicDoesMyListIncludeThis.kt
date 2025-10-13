
/**
 * [Enumerable Magic - Does My List Include This?](https://www.codewars.com/kata/545991b4cbae2a5fda000158/train/kotlin)
 *
 * Create a method that accepts a list and an item, and returns true if the item belongs to the list. Return false otherwise.
 */
//fun include(arr: List<Int>, item: Int): Boolean = arr.any { it == item }
//fun include(arr: List<Int>, item: Int): Boolean = item in arr
fun include(arr: List<Int>, item: Int): Boolean = arr.contains(item)
