use crate::model::ProductAggregate;
use crate::spec::{Aggregate, Command, CommandHandler};

pub enum ProductCommand {
    Create { sku: String, quantity: usize },
    Reserve { sku: String, quantity: usize },
    Release { sku: String, quantity: usize },
    Ship { sku: String, quantity: usize },
}

impl Command<String, ProductAggregate> for ProductCommand {
    fn id(&self) -> String {
        match self {
            Self::Create { sku, .. } => sku.clone(),
            Self::Reserve { sku, .. } => sku.clone(),
            Self::Release { sku, .. } => sku.clone(),
            Self::Ship { sku, .. } => sku.clone(),
        }
    }

    fn aggregate() -> ProductAggregate {
        ProductAggregate::new()
    }
}

impl ProductCommand {
    pub fn create(sku: &str, initial_quantity: usize) -> Self {
        Self::Create {
            sku: sku.to_owned(),
            quantity: initial_quantity,
        }
    }

    pub fn reserve(sku: &str, quantity: usize) -> Self {
        Self::Reserve {
            sku: sku.to_owned(),
            quantity: quantity,
        }
    }

    pub fn ship(sku: &str, quantity: usize) -> Self {
        Self::Ship {
            sku: sku.to_owned(),
            quantity: quantity,
        }
    }
}

impl CommandHandler for ProductCommand {
    type Item = Self;

    fn execute(&self, command: &Self::Item) {
        let aggregate = Self::aggregate();

        let result = match command {
            &Self::Create { ref sku, quantity } => aggregate.create(&sku.to_owned(), quantity),
            &Self::Reserve { quantity, .. } => aggregate.reserve(quantity),
            &Self::Release { quantity, .. } => aggregate.release(quantity),
            &Self::Ship { quantity, .. } => aggregate.ship(quantity),
        };

        match result {
            Ok(events) => {
                events.iter().fold(aggregate, |a, ref b| a.apply(b));
            }
            Err(error) => {
                //TODO Handle errors.
            }
        }
    }
}
