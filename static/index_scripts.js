
const instructors = ['John Doe', 'Jane Smith', 'Alice Johnson'];
const courses = ['Math 101', 'History 202', 'Biology 303'];

function search() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    let results = '';

    //search instructors
    for (const instructor of instructors) {
        if (instructor.toLowerCase().includes(input)) {
            results += `<p>${instructor}</p>`;
        }
    }

    //search courses
    for (const course of courses) {
        if (course.toLowerCase().includes(input)) {
            results += `<p>${course}</p>`;
        }
    }

    document.getElementById('results').innerHTML = results;
}
