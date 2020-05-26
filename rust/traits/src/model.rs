#[derive(Debug)]
pub struct Classroom {
    pub number: u8,
}

pub trait Repository {
    fn save(&mut self, classroom: Classroom);
    fn print(&self);
}

pub struct ClassroomRepo {
    data: Vec<Classroom>,
}

impl ClassroomRepo {
    pub fn new() -> Self {
        Self { data: vec![] }
    }
}

impl Repository for ClassroomRepo {
    fn save(&mut self, classroom: Classroom) {
        self.data.push(classroom);
    }

    fn print(&self) {
        for c in self.data.iter() {
            println!("{:?}", c);
        }
    }
}

pub struct Service<'a> {
    pub repo: &'a mut dyn Repository,
    pub service: &'a dyn GenericServiceTrait,
}

impl<'a> Service<'a> {
    pub fn new(repo: &'a mut dyn Repository, service: &'a dyn GenericServiceTrait) -> Self {
        let r = ClassroomRepo::new();
        // let service = GenericService::new(r);
        Self { repo, service }
    }

    pub fn create(&mut self, classroom: Classroom) {
        self.repo.save(classroom);
    }
}

// Created for encapsulates an struct with an attribute of generic struct type.alloc
// Enables the Service Struct receive a generic struct in service attribute.
pub trait GenericServiceTrait {}
pub struct GenericService<T: Repository> {
    pub repo: T,
}

impl<T: Repository> GenericServiceTrait for GenericService<T> {}

impl<T: Repository> GenericService<T> {
    pub fn new(repo: T) -> Self {
        Self { repo }
    }
}
