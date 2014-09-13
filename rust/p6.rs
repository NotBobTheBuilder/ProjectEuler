/// # Sum square difference
/// # Problem 6
/// The sum of the squares of the first ten natural numbers is
/// > 12 + 22 + ... + 102 = 385
/// The square of the sum of the first ten natural numbers is,
/// > (1 + 2 + ... + 10)2 = 552 = 3025
/// Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
/// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


use std::num::pow;
use std::iter::AdditiveIterator;

fn main() {
  let sum_squares = range(1, 101).map(|n| pow(n, 2)).sum();
  let squares_sum = pow(range(1, 101).sum(), 2);

  println!("{}", squares_sum - sum_squares );
}
