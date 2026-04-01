impl Solution {
    pub fn count_max_or_subsets(nums: Vec<i32>) -> i32 {
        let mut max_or = 0;
        for &num in &nums {
            max_or |= num;
        }

        let mut count = 0;
        for i in 0..(1 << nums.len()) {
            let mut current_or = 0;
            for j in 0..nums.len() {
                if (i & (1 << j)) != 0 {
                    current_or |= nums[j];
                }
            }
            if current_or == max_or {
                count += 1;
            }
        }

        count
        
    }
}