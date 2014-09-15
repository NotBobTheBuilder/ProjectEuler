/// # Special Pythagorean triplet
/// ## Problem 9
/// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
/// a2 + b2 = c2
/// For example, 32 + 42 = 9 + 16 = 25 = 52.
/// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
/// Find the product abc.

use std::num::pow;

fn main() {
    for b in range(1, 1001) {
        for a in range(1, b) {
            let c2 = pow(b, 2) + pow(a, 2);
            let c = (c2 as f64).sqrt();
            if c.fract() == 0.0 && a + b + (c as int) == 1000 {
                println!("{}", a * b * (c as int));
            }
        }
    }
}
