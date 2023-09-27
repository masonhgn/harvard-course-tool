import pandas as pd
from Course import Course
from Instructor import Instructor
import re


def generate_slug(name):
    # Convert to lowercase
    slug = name.lower()
    
    # Replace spaces with hyphens
    slug = slug.replace(" ", "-")
    
    # Remove non-alphanumeric characters (except for hyphens)
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    
    return slug

def format_name(name):
    last_name, first_name = name.split(',')
    return f"{first_name} {last_name}"


def process_courses(file_path, course_map, term):
    
    df = pd.read_csv(file_path, header=3).dropna()
    for index, row in df.iterrows():

        instructor_name = format_name(row['Instructor Full Name'])


        if row["Course ID"] in course_map:
            found_course = course_map[row["Course ID"]]

            #add instructor if not already added
            if instructor_name not in found_course.instructors:
                found_course.instructors.append(instructor_name)

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
                [instructor_name],
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
        




def process_instructors(file_path, instructor_map, term):
    df = pd.read_csv(file_path, header=3).dropna()
    for index, row in df.iterrows():

        ugrad_num = 0 if pd.isna(row['UGrad']) else int(row['UGrad'])
        grad_num = 0 if pd.isna(row['Grad']) else int(row['Grad'])
        nondegree_num = 0 if pd.isna(row['NonDegree']) else int(row['NonDegree'])
        xreg_num = 0 if pd.isna(row['XReg']) else int(row['XReg'])
        vus_num = 0 if pd.isna(row['VUS']) else int(row['VUS'])
        employee_num = 0 if pd.isna(row['Employee']) else int(row['Employee'])
        withdraw_num = 0 if pd.isna(row['Withdraw']) else int(row['Withdraw'])
        total_num = 0 if pd.isna(row['Total']) else int(row['Total'])

        instructor_name = format_name(row['Instructor Full Name'])

        #if instructor is already in map
        if instructor_name in instructor_map:
            found_instructor = instructor_map[instructor_name]

            #if course is already stored for that professor
            if row['Course ID'] in found_instructor.courses_taught:
                if not term in found_instructor.courses_taught[row['Course ID']]:
                    found_instructor.courses_taught[row['Course ID']].append(term)
            else: #course is not yet stored for that professor
                found_instructor.courses_taught[row['Course ID']] = [term]

            #add department for professor 
            if row['Course Department'] not in found_instructor.departments:
                found_instructor.departments.append(row['Course Department'])

            #add metrics for amount of students taught by semester

            #undergrad
            if term not in found_instructor.ugrad:
                found_instructor.ugrad[term] = ugrad_num
            else: found_instructor.ugrad[term] += ugrad_num

            #grad
            if term not in found_instructor.grad:
                found_instructor.grad[term] = grad_num
            else: found_instructor.grad[term] += grad_num

            #nondegree
            if term not in found_instructor.nondegree:
                found_instructor.nondegree[term] = nondegree_num
            else: found_instructor.nondegree[term] += nondegree_num

            #xreg
            if term not in found_instructor.xreg:
                found_instructor.xreg[term] = xreg_num
            else: found_instructor.xreg[term] += xreg_num

            #vus
            if term not in found_instructor.vus:
                found_instructor.vus[term] = vus_num
            else: found_instructor.vus[term] += vus_num

            #employee
            if term not in found_instructor.employee:
                found_instructor.employee[term] = employee_num
            else: found_instructor.employee[term] += employee_num


            #withdraw
            if term not in found_instructor.withdraw:
                found_instructor.withdraw[term] = withdraw_num
            else: found_instructor.withdraw[term] += withdraw_num

            #total
            if term not in found_instructor.total:
                found_instructor.total[term] = total_num
            else: found_instructor.total[term] += total_num




        else:
            #make an instructor
            instructor = Instructor(
                generate_slug(instructor_name),
                instructor_name,
                {row['Course ID']: [term]},
                [row['Course Department']],
                {term : ugrad_num},
                {term : grad_num},
                {term : nondegree_num},
                {term : xreg_num},
                {term : vus_num},
                {term : employee_num},
                {term : withdraw_num},
                {term : total_num},
            )

            instructor_map[instructor_name] = instructor
                



######## ACTUAL DATA INITIALIZATION ##########

def initialize_data():
    terms = ['spring2021', 'fall2021', 'spring2022', 'fall2022', 'spring2023', 'fall2023']

    courses = {}
    instructors = {}
    for term in terms:
        process_courses('csv/'+term+'.csv', courses, term)
        process_instructors('csv/'+term+'.csv', instructors, term)

    #print(instructors["Shieber,Stuart M."].to_dict())


    #gather every instructor and course object and put them together into one list to send to the database
    instructor_dicts = [instructors[instructor].to_dict() for instructor in instructors]
    course_dicts = [courses[course].to_dict() for course in courses]
    return [instructor_dicts, course_dicts]




