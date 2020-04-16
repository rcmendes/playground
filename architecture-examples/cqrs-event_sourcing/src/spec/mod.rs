mod commands;
mod events;
mod models;
mod queries;

pub use commands::*;
pub use events::*;
pub use models::*;
pub use queries::*;

pub trait DomainError: Sized {
    fn message() -> String;
}
