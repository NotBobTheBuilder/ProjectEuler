/// # 10001st prime
/// ## Problem 7
/// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
/// What is the 10 001st prime number?

use std::collections::TreeSet;

fn main() {
  let mut num = 3;
  let mut primes = TreeSet::<int>::new();
  primes.insert(2);

  while primes.len() != 10001 {
    if primes.iter().take_while(|&p| *p < num / 2).all(|&p| num % p != 0) {
      primes.insert(num);
    }
    num += 2;
  }
  println!("{}", primes.iter().nth(10000).unwrap())

}
