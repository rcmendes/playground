mod model;

use model::*;

fn main() {
    let mut repo = ClassroomRepo::new();
    let service = GenericService::new(ClassroomRepo::new());

    let mut service = Service::new(&mut repo, &service);

    let c1 = Classroom { number: 1 };
    let c2 = Classroom { number: 2 };
    let c3 = Classroom { number: 3 };

    service.create(c1);
    service.create(c2);
    service.create(c3);

    service.repo.print();
}

//References
// - https://stackoverflow.com/questions/40064700/vector-of-generic-structs-in-rust
// - https://tratt.net/laurie/blog/entries/a_quick_look_at_trait_objects_in_rust.html
// - https://brson.github.io/rust-anthology/1/all-about-trait-objects.html
