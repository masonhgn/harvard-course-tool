## Harvard EasySearch

https://harvardeasysearch.com

This is a search engine that I made specifically for Harvard, combining all courses and instructors into one easily queried database. My goal was to make it easier to find info about 
instructors and the courses they teach, and present it in a more modern and user friendly way than the real course directory.

Currently I only have data on the instructor names, the courses they've taught, which semesters they taught them and how many of each type of student were enrolled during each term, so that's the extent of what this site will provide as it relates to information.

The site uses the "Course Enrollment Stats" dataset from the Harvard Open Data Project.


I am not affiliated with Harvard in any way. I just wanted to make an interesting data driven project using Harvard's resources.



### Functionality/Stack
The website is built using Flask and MongoDB. There was no front-end framework used, the HTML/CSS/JS was all my own so please bear with me on any front-end related issues as I am still learning. 

I downloaded six of the most recent "Course Enrollment Stats" datasets from the Harvard Open Data Project site, and loaded them in data.py using pandas. There are two objects, Course and Instructor, which I've created specifically to make sense of the datasets, draw interesting metrics, and store everything in my Mongo database.



### Home Page:
![image](https://github.com/masonhgn/harvard-course-tool/assets/73012906/52a07a5a-f02b-4a12-b6f5-261f2ddf2780)


### Professor Detail Page:
![image](https://github.com/masonhgn/harvard-course-tool/assets/73012906/1c9f1d90-879e-40ec-a4af-e643510c66f8)


### Course Detail Page:
![image](https://github.com/masonhgn/harvard-course-tool/assets/73012906/593ea7f5-5ace-4fea-a1a2-c5616a834a33)


