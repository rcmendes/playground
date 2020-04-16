use std::time::Instant;

pub struct ProductEventData {
    pub sku: String,
    pub quantity: usize,
    pub timestamp: Instant,
}

pub enum ProductEvent {
    Created(ProductEventData),
    Released(ProductEventData),
    Reserved(ProductEventData),
    Shipped(ProductEventData),
}

impl ProductEvent {
    pub fn created(sku: &str, quantity: usize) -> Self {
        Self::Created(ProductEventData {
            sku: sku.to_owned(),
            quantity: quantity,
            timestamp: Instant::now(),
        })
    }

    pub fn reserved(sku: &str, quantity: usize) -> Self {
        Self::Reserved(ProductEventData {
            sku: sku.to_owned(),
            quantity: quantity,
            timestamp: Instant::now(),
        })
    }

    pub fn released(sku: &str, quantity: usize) -> Self {
        Self::Released(ProductEventData {
            sku: sku.to_owned(),
            quantity: quantity,
            timestamp: Instant::now(),
        })
    }

    pub fn shipped(sku: &str, quantity: usize) -> Self {
        Self::Shipped(ProductEventData {
            sku: sku.to_owned(),
            quantity: quantity,
            timestamp: Instant::now(),
        })
    }
}
