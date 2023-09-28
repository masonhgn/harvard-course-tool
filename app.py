from flask import Flask, render_template, request, url_for, redirect, jsonify
from pymongo import MongoClient
from data import generate_slug

from data import initialize_data, generate_slug
app = Flask(__name__)

#to start mongod on mac using home directory db folder:
#mongod --dbpath ~/mongodb-data

#anywhere else:
#mongod


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

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Query not provided"}), 400

    # Query the courses and instructors (limiting to 10 results each for example)
    courses = list(courses_collection.find({"course_name": {"$regex": query, "$options": "i"}}).limit(10))
    instructors = list(instructors_collection.find({"name": {"$regex": query, "$options": "i"}}).limit(10))

    # Convert MongoDB results to a list of dictionaries (ignoring ObjectId)
    courses_results = [{"course_name": c["course_name"]} for c in courses]
    instructors_results = [{"name": i["name"]} for i in instructors]

    return jsonify({"courses": courses_results, "instructors": instructors_results})

@app.route('/', methods=('GET', 'POST'))
def index():
    course_names = ['(' + course['course_title'] + ') ' + course['course_name'] + ' [' +course['course_id'] + ']' for course in courses_collection.find()]
    instructor_names = [instructor['name'] for instructor in instructors_collection.find()]
    collection = course_names + instructor_names
    return render_template('index.html', collection=collection)


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


@app.route('/slugify', methods=['POST'])
def slugify():
    instructor_name = request.form.get('instructor_name')
    # Use your existing slugify function to generate the slug
    slug = generate_slug(instructor_name)
    return slug

@app.context_processor
def utility_processor():
    def slugify(instr):
        return generate_slug(instr)
    return dict(generate_slug=slugify)
