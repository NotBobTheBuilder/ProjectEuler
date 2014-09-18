/*
 * # 10001st prime
 * ## Problem 7
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 * What is the 10 001st prime number?
 */

import scala.math.sqrt

object Euler7 {
    val primes: Stream[Int] = 2 #:: Stream.from(3).filter({ n => primes.takeWhile(_ <= sqrt(n)).forall(n % _ != 0) })
    def main(args: Array[String]) {
        println(primes(10000))
    }
}
