use futures::future::{BoxFuture, FutureExt};
use std::path::Path;
use tokio::fs;
use tokio::prelude::*;

#[tokio::main]
async fn main() {
    println!("Async tests in Rust with Tokio.");

    // let file = Path::new("/Users/rodrigo/Downloads/NeatReader-5.0.1.dmg");
    let file = Path::new("/Users/rodrigo/Downloads/credentials.csv");
    print_file_data(file).await;

    let dir = Path::new("/Users/rodrigo/Downloads");
    print_files_from_dir(dir).await;
}

fn print_files_from_dir<'a>(dir: &'a Path) -> BoxFuture<'a, ()> {
    async move {
        if let Ok(mut entries) = fs::read_dir(dir).await {
            while let Ok(next_entry) = entries.next_entry().await {
                if let Some(entry) = &next_entry {
                    if let Ok(metadata) = entry.metadata().await {
                        if metadata.is_file() && metadata.len() >= 1 {
                            println!("> {:?} | {}", &entry.path(), metadata.len());
                        } else if metadata.is_dir() {
                            print_files_from_dir(&entry.path()).await;
                        }
                    }
                } else {
                    break;
                }
            }
        }
    }
    .boxed()
}

async fn print_file_data(file: &Path) {
    match fs::read(file).await {
        Ok(data) => println!(
            "--------------------\n{}\n--------------------",
            String::from_utf8_lossy(&data)
        ),
        Err(e) => println!("Error: {}", e),
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
