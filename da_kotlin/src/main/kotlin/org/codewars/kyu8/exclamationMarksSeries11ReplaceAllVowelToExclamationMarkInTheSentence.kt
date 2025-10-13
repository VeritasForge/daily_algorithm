
/**
 * [Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence](httpshttps://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/kotlin)
 *
 * Description:
 * Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
 *
 * Examples
 * replace("Hi!") === "H!!"
 * replace("!Hi! Hi!") === "!H!! H!!"
 * replace("aeiou") === "!!!!!"
 * replace("ABCDE") === "!BCD!"
 */
//fun replace(s: String): String = s.replace(Regex("[aeiouAEIOU]"), "!")
//fun replace(s: String): String = s.replace(Regex("[aeiou]", RegexOption.IGNORE_CASE), "!")
fun replace(s: String): String = s.replace(Regex("a|e|i|o|u", RegexOption.IGNORE_CASE), "!")
