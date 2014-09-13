/// # Multiples of 3 and 5
/// ## Problem 1
/// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
/// Find the sum of all the multiples of 3 or 5 below 1000.

fn main() {
    let mut total = 0;

    for n in range(1, 1000) {
        match n {
            v if v % 3 == 0 => total += v,
            v if v % 5 == 0 => total += v,
            _ => { /* do nothing */ }
        }
    }

    println!("result is {}", total);

}
