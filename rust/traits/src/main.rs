#[derive(Debug)]
struct Classroom {
    pub number: u8,
}

trait Repository {
    fn save(&mut self, classroom: Classroom);
    fn print(&self);
}

struct ClassroomRepo {
    pub data: Vec<Classroom>,
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

struct Service<'a> {
    repo: &'a mut dyn Repository, // repo: Box<&'a dyn Repository>
}

impl<'a> Service<'a> {
    pub fn new(repo: &'a mut (dyn Repository + 'a)) -> Self {
        // let repo = Box::new(repo);
        Self { repo }
    }

    pub fn create(&mut self, classroom: Classroom) {
        self.repo.save(classroom);
    }
}

fn main() {
    let mut repo = ClassroomRepo { data: vec![] };

    let mut service = Service::new(&mut repo);

    let c1 = Classroom { number: 1 };
    let c2 = Classroom { number: 2 };
    let c3 = Classroom { number: 3 };

    service.create(c1);
    service.create(c2);
    service.create(c3);

    service.repo.print();
}
