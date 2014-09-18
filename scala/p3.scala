/*
 * 10001st prime
 * Problem 7
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 * What is the 10 001st prime number?
 */

import scala.math.sqrt

object Euler3 {
    val primes: Stream[Int] = 2 #:: Stream.from(3).filter({ p => primes.takeWhile(_ <= sqrt(p)).forall(p % _ != 0) })
    
    def factors(num: Long): List[Long] = {
        primes.takeWhile(_ <= sqrt(num)).find(num % _ == 0) match {
            case Some(p) => p :: factors(num / p)
            case None => List(num)
        }
    }

    def main(args: Array[String]) {
        println(factors(600851475143L).max)
    }
}
