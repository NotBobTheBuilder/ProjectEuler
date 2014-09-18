/*
 * # Largest palindrome product
 * ## Problem 4
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */

object Euler4 {
    implicit class Palindrome[Int](n: Int) {
        def isPalindromic(): Boolean = {
            n.toString == n.toString.reverse
        }
    }

    def main(args: Array[String]) {
        println(100.to(999).map({ n =>
            val palindromicProducts = n.to(999).map(_*n).filter(_.isPalindromic())
            if (palindromicProducts.length == 0) {0} else {palindromicProducts.max}
        }).max)
    }
}
