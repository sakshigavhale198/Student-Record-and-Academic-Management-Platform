# Enterprise Student Record & Academic Management Platform

## Project Overview
The Enterprise Student Record and Academic Management Platform is a containerized application built with Python and Flask, featuring automated unit testing and a GitHub-based CI/CD pipeline. Developed by Sakshi Gavhale (PRN: 2125UDSF1111), the platform streamlines academic administration through scalable digital workflows.

## Tech Stack
* Backend: Python 3.11, Flask
* Testing: Pytest
* Containerization: Docker
* CI/CD & Version Control: GitHub Actions, Git

---

## Agile Scrum Documentation

### Epics & User Stories

#### Epic 1: Student Record & Profile Management
* User Story 1.1: As an administrator, I want to register new student profiles (name, course, GPA) into the system so that academic records are accurately maintained.
* User Story 1.2: As an administrator, I want to view the complete list of registered students to track active enrollments.

#### Epic 2: Academic Grading & Course Management
* User Story 2.1: As a student or faculty member, I want to view enrolled courses and academic standing.
* User Story 2.2: As an automated testing pipeline, I want to execute unit tests using pytest on every code push to ensure system stability.

---

## Architecture & Modules
The platform’s architecture integrates key administrative modules:
* Student Registration Module: Handles adding and retrieving student details.
* Course Management Module: Tracks course assignments and academic standing.
* Containerization Module: Ensures seamless deployment across local and cloud environments (AWS EC2).

## Running the Application Locally / via Docker
1. Build the Docker Image:
   
