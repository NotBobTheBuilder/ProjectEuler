/// # Largest palindrome product
/// ## Problem 4
/// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
/// Find the largest palindrome made from the product of two 3-digit numbers.

fn is_palindrome(n: int) -> bool {
  let fwd = n.to_str().into_bytes();
  let mut rev = fwd.clone();
  rev.reverse();

  let mut chars = fwd.iter().zip(rev.iter());

  chars.all(|(a,b)| a == b)
}

fn main() {
  let mut largest = 0;
  for a in range(100, 1000) {
    for b in range(100, 1000) {
      let product = a * b;
      if is_palindrome(product) {
        largest = if largest > product {largest} else {product}
      }
    }
  }
  println!("largest: {}", largest);
}
