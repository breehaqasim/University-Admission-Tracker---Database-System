# University-Admission-Tracker---Database-System
The University Admission Tracker Database Management System is an ambitious project
aimed at simplifying the complex process of applying to universities. Its primary scope is to
create an accessible and user-friendly platform for students to search for universities in a
specific country and city, while also allowing them to refine their choices based on admission
criteria such as SAT scores, academic records, and other relevant factors and also can contact
counselors. This platform is designed to simplify the complex process of exploring and selecting
universities for students amidst preparations for their boards/CAIE’s. By doing so, it not only
saves time but also facilitates the process of narrowing down options, making it easier for each
student to find their ideal university.
This system aims to provide students with a powerful tool to make informed decisions about
their higher education journey by offering detailed university profiles that include critical
information like admission prerequisites, university type, average annual cost of university,
acceptance rate, application deadlines, campus locations, website link and contact details.
By encompassing these features, this project aims to empower students and streamline their
university application process, ultimately helping them find the institutions where they best fit
and meet the admission requirements.


## Instructions
- User should've downloaded PyQt6 and pyodbc to run this file
- Also they shouldve MYSQL software on their desktop run the skeleton sql script provided to you then
- To run the file click Play Button (Run Python File)

## How our application works?
- Once user run's python file two options will be displayed Student and Administrator
- If User selects **Administrator** option s/he will be able to explore the Administrator Functionalities
- If Admin User is old admin and he has registred before s/he can use his or her credentials to login on our application only then s/he will be able 
to "Edit University Details" of existing university data
- Once Admin Logs In Admin Dashboard will appear which will show READ ONLY data of his/her university then s/he can click "Edit Now" button if s/he wishes to edit any detail
- If Admin User is new admin s/he will have to register on our application, to do so s/he will enter email and password and click "Register" Button to register themselves
- A new screen will pop up to new admin and now the new admin is supposed to "Add University Details" s/he will then add their university on our database.
- If User selects **Student** option s/he will be able to explore Student Functionalities
- If Student has used our application before then s/he will simply need to Login on our application using his or her credentials.
- If Student has never used our application before then s/he will click "Sign Up" button a "Registration Form" will appear which s/he will have to fill
- Once student has successfully Logged In/Registred s/he will get access to all functionalities
- A Student Dashboard will appear
- A Student can click on "Search University" to search for universities a new screen will appear
- Student enter the criteria s/he wishes to filter from then once Student clicks "Search Button" Universities will populate in table below
- Student can click any University then click "View" button a new screen will pop up where the University details will be shown to Student
- Another feature we are providing to Student is of Searching Counsellors
- If Student wishes to search for counsellors s/he can return back to Student Dashboard 
- Now if Student clicks "Contact Counsellors" a new screen will appear where Student can filter by Country, once Student clicks "Search" Button the table will get populated
