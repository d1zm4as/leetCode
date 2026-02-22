pub fn is_prime(x: u64) -> bool {
    if x == 2 {return true};
    if x < 2 || x % 2 == 0 {return false};
    (3..).step_by(2).take_while(|i| i*i <= x).all(|i| x % i != 0)
}


impl Solution {
    pub fn count_primes(n: i32) -> i32 {
        (2..n as u64).filter(|&x| is_prime(x)).count() as i32
    }
}