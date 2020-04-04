use rand::prelude::*;
use std::cmp::Ordering;
use std::io;

pub fn guess_game() {
    println!("Starting Guess game!\n\n");

    let secret_number = thread_rng().gen_range(1, 101);

    loop {
        println!("Please inform your guess:");
        let mut guess = String::new();

        io::stdin().read_line(&mut guess).expect("Fail to read");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Greater => println!("To big!"),
            Ordering::Less => println!("Too small!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
