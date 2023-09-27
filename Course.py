


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


    # Any additional methods or functionalities can be added below
