USE experiment;
SELECT * FROM major;
SELECT * FROM student;
SELECT * FROM Major_Student;


USE experiment;
SELECT S_name FROM student,major,Major_Student
WHERE S_from="浙江" AND 
Major_Student.S_number=student.S_number AND 
Major_Student.M_number=major.M_number AND
M_name ="物联网" AND class="二班";
