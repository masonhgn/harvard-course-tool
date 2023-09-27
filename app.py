from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from data import initialize_data, generate_slug
app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos

instructors, courses = initialize_data()




instructors_collection = db["instructors"]
courses_collection = db["courses"]


'''
instructors_collection.insert_many(instructors)
courses_collection.insert_many(courses)
'''




@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html', num_instructors = len(instructors))


@app.route('/instructors', methods=['GET'])
def instructors_list():
    all_instructors = list(instructors_collection.find())
    return render_template('instructors_list.html', instructors=all_instructors)



@app.route('/instructor/<slug>', methods=['GET'])
def instructor(slug):
    # Assuming the instructor's collection has a 'slug' field to match against
    instructor_data = instructors_collection.find_one({'slug': slug})
    if instructor_data:
        # Render the instructor's data using a template
        return render_template('instructor.html', instructor=instructor_data)
    else:
        # Alternatively, return a 404 error if the instructor is not found
        return "Instructor not found", 404



@app.context_processor
def utility_processor():
    def slugify(instr):
        return generate_slug(instr)
    return dict(generate_slug=slugify)


@app.route('/course/<course_id>')
def course_details(course_id):
    # Fetch the course object from the database using course_id
    course = courses_collection.find_one({"course_id": course_id})
    if not course:
        return "Course not found", 404

    return render_template('course.html', course=course)


@app.route('/courses')
def all_courses():
    # Fetch all the courses from the database
    courses = list(courses_collection.find())

    return render_template('courses_list.html', courses=courses)
