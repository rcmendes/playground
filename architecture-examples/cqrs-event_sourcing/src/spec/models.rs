pub trait Entity {
    type Item;

    fn id(&self) -> Self::Item
    where
        Self::Item: Sized;
}

pub trait Aggregate {
    type Item;

    fn version(&self) -> u64;

    fn apply(self, evt: &Self::Item) -> Self
    where
        Self: Sized;

    fn new() -> Self;
}
