


class Course:
    def __init__(self, 
                 course_id, 
                 course_title, 
                 course_name, 
                 course_section_code, 
                 course_department,
                 instructors,
                 ugrad,
                 grad,
                 nondegree,
                 xreg,
                 vus,
                 employee,
                 withdraw,
                 total):

        self.course_id = course_id
        self.course_title = course_title
        self.course_name = course_name
        self.course_section_code = course_section_code
        self.course_department = course_department
        self.instructors = instructors
        self.ugrad = ugrad
        self.grad = grad
        self.nondegree = nondegree
        self.xreg = xreg
        self.vus = vus
        self.employee = employee
        self.withdraw = withdraw
        self.total = total


    def __str__(self):
        instructor_names = ', '.join([instr for instr in self.instructors])
        return (f"Course ID: {self.course_id}\n"
                f"Course Title: {self.course_title}\n"
                f"Course Name: {self.course_name}\n"
                f"Course Section Code: {self.course_section_code}\n"
                f"Course Department: {self.course_department}\n"
                f"Instructors: {instructor_names}\n"
                f"UGrad Enrollments: {self.ugrad}\n"
                f"Grad Enrollments: {self.grad}\n"
                f"Non-Degree Enrollments: {self.nondegree}\n"
                f"XReg Enrollments: {self.xreg}\n"
                f"VUS Enrollments: {self.vus}\n"
                f"Employee Enrollments: {self.employee}\n"
                f"Withdrawals: {self.withdraw}\n"
                f"Total Enrollments: {self.total}")

    def to_dict(self):
        return self.__dict__
