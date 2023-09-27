


class Instructor:
    def __init__(self,
                 slug, 
                 name, 
                 courses_taught, 
                 departments, 
                 ugrad, 
                 grad, 
                 nondegree, 
                 xreg, 
                 vus, 
                 employee, 
                 withdraw, 
                 total):

        self.slug = slug
        self.name = name
        self.courses_taught = courses_taught or {}  
        self.departments = departments or []
        self.ugrad = ugrad or {}
        self.grad = grad or {}
        self.nondegree = nondegree or {}
        self.xreg = xreg or {}
        self.vus = vus or {}
        self.employee = employee or {}
        self.withdraw = withdraw or {}
        self.total = total or {}

    def __str__(self):
        return (f"Instructor Name: {self.name}\n"
                f"Instructor Slug: {self.slug}\n"
                f"Courses Taught: {self.courses_taught}\n"
                f"Departments: {', '.join(self.departments)}\n"
                f"Undergrads: {self.ugrad}\n"
                f"Grads: {self.grad}\n"
                f"NonDegree Students: {self.nondegree}\n"
                f"XReg Students: {self.xreg}\n"
                f"VUS Students: {self.vus}\n"
                f"Employees: {self.employee}\n"
                f"Withdrawals: {self.withdraw}\n"
                f"Total Enrollments: {self.total}\n")

    def to_dict(self):
        return self.__dict__

