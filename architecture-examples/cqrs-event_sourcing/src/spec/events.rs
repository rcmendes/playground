use super::DomainError;

pub trait Event {}

pub trait EventListener {
    type Data;
    type Error;
    fn handle(evt: dyn Event) -> Result<Self::Data, Self::Error>
    where
        Self::Error: DomainError;
}
