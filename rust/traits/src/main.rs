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
