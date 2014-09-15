/// # Summation of primes
/// ## Problem 10
/// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
/// Find the sum of all the primes below two million.

use std::collections::TreeSet;
use std::iter::AdditiveIterator;

fn main() {
    let mut num = 3;
    let mut primes = TreeSet::<int>::new();
    primes.insert(2);

    while num < 2000000 {
        if primes.iter().take_while(|&p| *p < ((num as f64).sqrt() + 1.0) as int).all(|&p| num % p != 0) {
            primes.insert(num);
        }
        num += 2;
    }
    println!("{}", primes.iter().map(|&n| n).sum())
}
