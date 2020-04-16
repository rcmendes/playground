use crate::events::{ProductEvent, ProductEventData};
use crate::spec::Aggregate;

pub enum ProductError {
    RequestedQuantityNotAvailable {
        available_quantity: usize,
        requested_quantity: usize,
    },
    ProductNotCreated,
}

pub struct ProductAggregate {
    sku: String,
    available_quantity: usize,
    version: u64,
}

impl ProductAggregate {
    pub fn create(&self, sku: &str, quantity: usize) -> Result<Vec<ProductEvent>, ProductError> {
        Ok(vec![ProductEvent::created(sku, quantity)])
    }

    pub fn reserve(&self, quantity: usize) -> Result<Vec<ProductEvent>, ProductError> {
        if self.version == 0 {
            return Err(ProductError::ProductNotCreated);
        }

        if self.available_quantity < quantity {
            return Err(ProductError::RequestedQuantityNotAvailable {
                available_quantity: self.available_quantity,
                requested_quantity: quantity,
            });
        }

        Ok(vec![ProductEvent::reserved(&self.sku, quantity)])
    }

    pub fn release(&self, quantity: usize) -> Result<Vec<ProductEvent>, ProductError> {
        Ok(vec![ProductEvent::released(&self.sku, quantity)])
    }

    pub fn ship(&self, quantity: usize) -> Result<Vec<ProductEvent>, ProductError> {
        Ok(vec![ProductEvent::shipped(&self.sku, quantity)])
    }
}

impl Aggregate for ProductAggregate {
    type Item = ProductEvent;

    fn version(&self) -> u64 {
        self.version
    }

    fn apply(mut self, evt: &ProductEvent) -> Self {
        use ProductEvent::*;

        self.sku = match &evt {
            &Created(ProductEventData { sku, .. }) => sku.clone(),
            _ => self.sku,
        };

        self.version += 1;

        self.available_quantity = match evt {
            &Created(ProductEventData { quantity, .. }) => quantity,
            &Reserved(ProductEventData { quantity, .. }) => self.available_quantity - quantity,
            &Released(ProductEventData { quantity, .. }) => self.available_quantity + quantity,
            _ => self.available_quantity,
        };

        self
    }

    fn new() -> Self {
        Self {
            sku: "".to_owned(),
            available_quantity: 0,
            version: 0,
        }
    }
}
