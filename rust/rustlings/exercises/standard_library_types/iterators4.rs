// iterators4.rs

pub fn factorial(num: u64) -> u64 {
    if num > 1 {
        num * factorial(num - 1)
    } else {
        1
    }
}

fn factorial2(n: u64) -> u64 {
    (1..).take_while(|&i| i <= n).product()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn factorial_of_1() {
        assert_eq!(1, factorial(1));
    }
    #[test]
    fn factorial_of_2() {
        assert_eq!(2, factorial(2));
    }

    #[test]
    fn factorial_of_4() {
        assert_eq!(24, factorial(4));
    }
}