impl Solution{
    pub fn sum_zero(n: i32) -> Vec<i32> {
        let mut result = Vec::new();
        for i in 1..=n/2 {
            result.push(i);
            result.push(-i);
        }
        if n % 2 != 0 {
            result.push(0);
        }
        result
    }
}