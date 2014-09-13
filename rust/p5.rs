/// # Smallest multiple
/// ## Problem 5
/// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
/// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

fn main() {
  let mut numerator = 22;
  loop {
    if range(1, 21).all(|n| numerator % n == 0) {
      break;
    }
    numerator += 2;
  }
  println!("smallest multiple: {}", numerator);
}
