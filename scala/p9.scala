/* 
 * # Special Pythagorean triplet
 * ## Problem 9
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
 * a2 + b2 = c2
 * For example, 32 + 42 = 9 + 16 = 25 = 52.
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 */

import scala.math.{ pow, sqrt }

object Euler9 {
    def main(args: Array[String]) {
        val triplets = 1.to(1000).flatMap({ a =>
            1.to(999 - a).map({ b => (a, b, sqrt(pow(a, 2) + pow(b, 2))) })
        })
        triplets.find { case (a, b, c) => a + b + c == 1000 } match {
            case Some((a, b, c)) => println("%f".format(a * b * c))
            case None => println("Pythagoras Lied")
        }
    }
}
