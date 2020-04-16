use super::models::Aggregate;

pub trait Command<ID: Sized, T: Aggregate> {
    fn id(&self) -> ID;
    fn aggregate() -> T;
}

pub trait CommandHandler {
    type Item;
    fn execute(&self, command: &Self::Item)
    where
        Self: Sized;

    // fn load()
}
