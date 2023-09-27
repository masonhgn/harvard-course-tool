import pandas as pd
from Course import Course




def process_courses(file_path, course_map, term):
    
    df = pd.read_csv(file_path, header=3)
    for index, row in df.iterrows():

        if row["Course ID"] in course_map:
            found_course = course_map[row["Course ID"]]

            #add instructor if not already added
            if row["Instructor Full Name"] not in found_course.instructors:
                found_course.instructors.append(row["Instructor Full Name"])

            #add enrollment numbers for undergrad
            if term in found_course.ugrad: found_course.ugrad[term] += row["UGrad"]
            else: found_course.ugrad[term] = row["UGrad"]

            #add enrollment numbers for grad
            if term in found_course.grad: found_course.grad[term] += row["Grad"]
            else: found_course.grad[term] = row["Grad"]

            #add enrollment numbers for nondegree
            if term in found_course.nondegree: found_course.nondegree[term] += row["NonDegree"]
            else: found_course.nondegree[term] = row["NonDegree"]

            #add enrollment numbers for xreg
            if term in found_course.xreg: found_course.xreg[term] += row["XReg"]
            else: found_course.xreg[term] = row["XReg"]

            #add enrollment numbers for vus
            if term in found_course.vus: found_course.vus[term] += row["VUS"]
            else: found_course.vus[term] = row["VUS"]

            #add enrollment numbers for employee
            if term in found_course.employee: found_course.employee[term] += row["Employee"]
            else: found_course.employee[term] = row["Employee"]

            #add enrollment numbers for withdrawal
            if term in found_course.withdraw: found_course.withdraw[term] += row["Withdraw"]
            else: found_course.withdraw[term] = row["Withdraw"]

            #add enrollment numbers for total
            if term in found_course.total: found_course.total[term] += row["Total"]
            else: found_course.total[term] = row["Total"]

        else: #add course to course map
            course = Course(
                row["Course ID"],
                row['Course Title'],
                row['Course Name'],
                row['Course Section Code'],
                row['Course Department'],
                [row['Instructor Full Name']],
                {term : row['UGrad']},
                {term : row['Grad']},
                {term : row['NonDegree']},
                {term : row['XReg']},
                {term : row['VUS']},
                {term : row['Employee']},
                {term : row['Withdraw']},
                {term: row['Total']}
            )
            course_map[row["Course ID"]] = course
        

terms = ['spring2021', 'fall2021', 'spring2022', 'fall2022', 'spring2023', 'fall2023']



# Using the function:
courses = {}

for term in terms:
    process_courses('csv/'+term+'.csv', courses, term)

print(len(courses))

for course in courses:
    print(courses[course])
    break