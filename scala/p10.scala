/*
 * # Summation of primes
 * ## Problem 10
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 * Find the sum of all the primes below two million.
*/

import scala.math.sqrt

object Euler10 {
    val primes: Stream[Int] = 2 #:: Stream.from(3).filter({ n => primes.takeWhile(_ <= sqrt(n)).forall(n % _ != 0) })
    def main(args: Array[String]) {
        println(primes.takeWhile(_ < 2000000).map(_.toLong).sum)
    }
}
