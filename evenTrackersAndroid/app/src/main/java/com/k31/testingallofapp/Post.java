package com.k31.testingallofapp;

import com.google.gson.annotations.SerializedName;

public class Post {
    private Integer id;
    private String name;

    @SerializedName("student_id")
    private int studentId;

    @SerializedName("programme_code")
    private String programmeCode;
    private String faculty;
    private String campus;
    private String location;
    private String time;

    @SerializedName("class_attended")
    private String classAttended;
    private String lecturer;
    private String unique;


    //constructor
    public Post(String name, int studentId, String programmeCode, String faculty, String campus, String location, String time, String classAttended, String lecturer, String unique) {
        this.name = name;
        this.studentId = studentId;
        this.programmeCode = programmeCode;
        this.faculty = faculty;
        this.campus = campus;
        this.location = location;
        this.time = time;
        this.classAttended = classAttended;
        this.lecturer = lecturer;
        this.unique = unique;
    }

    //getter

    public Integer getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getStudentId() {
        return studentId;
    }

    public String getProgrammeCode() {
        return programmeCode;
    }

    public String getFaculty() {
        return faculty;
    }

    public String getCampus() {
        return campus;
    }

    public String getLocation() {
        return location;
    }

    public String getTime() {
        return time;
    }

    public String getClassAttended() {
        return classAttended;
    }

    public String getLecturer() {
        return lecturer;
    }

    public String getUnique() {
        return unique;
    }
}
