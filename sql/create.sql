DROP DATABASE if exists experiment;
CREATE DATABASE experiment;
USE  experiment;

/*
教师(教职工号，姓名，性别，出生年月，职称，教研室，电话号码)
*/
CREATE TABLE teacher(
    T_number CHAR(20) primary key,
    T_name CHAR(5),
    T_sex CHAR(20),
    T_brith CHAR(20),
    T_title CHAR(20),
    T_room CHAR(20),
    T_phone CHAR(20)
);

/*
课程(课程号，课程名，学时)
*/
CREATE TABLE lesson(
    L_number CHAR(20) primary key,
    L_name CHAR(20),
    L_time INT
);


/*
专业(专业代码，专业名称)
*/
CREATE TABLE major(
    M_number CHAR(20) primary key,
    M_name CHAR(20)
);


/*
学生(学号，姓名，性别，出生年月，籍贯)
*/
CREATE TABLE student(
    S_number CHAR(20) primary key,
    S_name char(20),
    S_sex CHAR(20),
    S_brith CHAR(20),
    S_from CHAR(20)
);

/*
设置(专业代码，课程号)
*/
CREATE table Major_Lesson(
    M_number CHAR(20),
    L_number CHAR(20),
    primary key(M_number, L_number),
    foreign key(M_number) references major(M_number),
    foreign key(L_number) references lesson(L_number)
);

/*
归属(专业代码，学号，班级)
*/
CREATE TABLE Major_Student(
    M_number CHAR(20),
    S_number CHAR(20),
    class CHAR(5),
    primary key(M_number,S_number),
    foreign key(M_number) references major(M_number),
    foreign key(S_number) references student(S_number)
);
CREATE TABLE Student_Lesson(
    S_number CHAR(20),
    L_number CHAR(20),
    GRADE CHAR(20),
    primary key(S_number,L_number),
    foreign key(S_number) references student(S_number),
    foreign key(L_number) references lesson(L_number)
);

CREATE TABLE Tecaher_Lesson(
    T_number CHAR(20),
    L_number CHAR(20),
    primary key(T_number,L_number),
    foreign key(T_number) references teacher(T_number),
    foreign key(L_number) references lesson(L_number)
);