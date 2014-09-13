/// ### Largest prime factor
/// ## Problem 3
/// The prime factors of 13195 are 5, 7, 13 and 29.
///
/// What is the largest prime factor of the number 600851475143 ?

use std::collections::TreeSet;

fn factors(num: int) -> Option<(int, int)> {
  for divisor in range(2, num / 2) {
    if num % divisor == 0 {
      return Some((divisor, num / divisor))
    }
  }
  None
}

fn prime_factors(num: int) -> TreeSet<int> {
  let mut numerator = num;
  let mut primes = TreeSet::<int>::new();

  loop {
    match factors(numerator) {
      Some((a, b)) => {
        primes.insert(a);
        numerator = b;
      }
      None => {
        primes.insert(numerator);
        return primes
      }
    }
  }
}

fn main() {
  let num = 600851475143;
  println!("{}", prime_factors(num).iter().max().unwrap());
}
