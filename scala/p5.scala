/*
 * # Smallest multiple
 * ## Problem 5
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 */

object Euler5 {
    def main(args: Array[String]) {
       println(Iterator.from(20, 2).find({ n => 1.to(20).forall(n % _ == 0) }))
    }
}
