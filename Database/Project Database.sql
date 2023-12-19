CREATE TABLE Administrator (
    Admin_ID INTEGER PRIMARY KEY IDENTITY(1,1),
    Admin_Email VARCHAR(255),
    Admin_Password VARCHAR(255)
);

CREATE TABLE Students (
    Student_ID INTEGER PRIMARY KEY IDENTITY(1,1),
    Student_Email VARCHAR(255),
    Student_Password VARCHAR(255),
	Student_Name varchar(255)
);


CREATE TABLE University (
    University_ID INTEGER PRIMARY KEY IDENTITY(1,1),
    University_Name VARCHAR(255),
    University_City VARCHAR(255),
	University_Country VARCHAR(255),
    /*Programs_Offered VARCHAR(255),*/
    Entry_Test VARCHAR(255),/*should be bool*/
    Acceptance_Rate float,
    SAT_score integer,
    Avg_Annual_Cost varchar(225),
    University_Type VARCHAR(255),
    Admin_ID INTEGER,
    FOREIGN KEY (Admin_ID) REFERENCES Administrator(Admin_ID)
);
CREATE TABLE Counsellor (
	Counsellor_Name VARCHAR(255),
    Contact_Email VARCHAR(255),
    Contact_Number VARCHAR(255),
	country varchar(255),
	Counsellor_id INTEGER PRIMARY KEY IDENTITY(1,1)
);

--insert one Admin to check the login functionality
select * from Administrator
set IDENTITY_INSERT Administrator on
insert into Administrator(Admin_ID,Admin_Email,Admin_Password) values (08283,'ahmed@gmail.com','a1234')
insert into Administrator(Admin_ID,Admin_Email,Admin_Password) values (08284,'fatima@gmail.com','f1235')
insert into Administrator(Admin_ID,Admin_Email,Admin_Password) values (08292,'breeha@gmail.com','b1234')
insert into Administrator(Admin_ID,Admin_Email,Admin_Password) values (08293,'safiah@gmail.com','s1234')
insert into Administrator(Admin_ID,Admin_Email,Admin_Password) values (08295,'nadia@gmail.com','f1238')

set IDENTITY_INSERT Administrator off


--insert one student to check the login functionality
SET IDENTITY_INSERT Students On;
insert into Students(Student_ID,Student_Email,Student_Password,Student_Name) values (011,'nimra@gmail.com','n678','Nimra')
insert into Students(Student_ID,Student_Email,Student_Password,Student_Name) values (014,'hunain@gmail.com','hu1234','Hunain')
insert into Students(Student_ID,Student_Email,Student_Password,Student_Name) values (015,'hammad@gmail.com','h9087','hammad malik')
insert into Students(Student_ID,Student_Email,Student_Password,Student_Name) values (016,'hamda@gmail.com','h5432','Hamda Basit')
insert into Students(Student_ID,Student_Email,Student_Password,Student_Name) values (017,'hassan@yahoo.com','h6789','Hassan Nizami')
SET IDENTITY_INSERT Students Off;
select * from Students

--insert one University to check the login functionality of Admin as its connected to university
SET IDENTITY_INSERT University On;
insert into  University(University_ID,University_Name,University_City,University_Country,Entry_Test,Acceptance_Rate,SAT_score,Avg_Annual_Cost,University_Type,Admin_ID) values (01,'Habib University','Karachi','Pakistan','SAT/HU Entry Test',55,1400,'PKR1209900','Private',08283)
insert into  University(University_ID,University_Name,University_City,University_Country,Entry_Test,Acceptance_Rate,SAT_score,Avg_Annual_Cost,University_Type,Admin_ID) values (02,'Stanford University','Stanford','United States','SAT/ACT',4.3,1465,'US$74700','Private',08284)
insert into  University(University_ID,University_Name,University_City,University_Country,Entry_Test,Acceptance_Rate,SAT_score,Avg_Annual_Cost,University_Type,Admin_ID) values (03,'University of Oxford','Oxford','United Kingdom','SAT/ACT/Oxford Entry Test',17.5,1480,'£9259','Public',08292)
insert into  University(University_ID,University_Name,University_City,University_Country,Entry_Test,Acceptance_Rate,SAT_score,Avg_Annual_Cost,University_Type,Admin_ID) values (04,'Melbourne University','Melbourne','Australia','SAT/ACT/Melbourne Entry Test',70,1300,'AUS$32000','Public',08293)
insert into  University(University_ID,University_Name,University_City,University_Country,Entry_Test,Acceptance_Rate,SAT_score,Avg_Annual_Cost,University_Type,Admin_ID) values (05,'Bogazici University','Istanbul','Turkey','YKS',20,1450,'TL 567,75 ','Public',08295)

SET IDENTITY_INSERT University Off;
select * from University

--insert counsellor information
SET IDENTITY_INSERT Counsellor On;
insert into Counsellor(Counsellor_Name,Contact_Email,Contact_Number,country,Counsellor_id) values ('Sarah Faisal','sarah@gmail.com','923355562218','Pakistan',112)
insert into Counsellor(Counsellor_Name,Contact_Email,Contact_Number,country,Counsellor_id) values ('George Bush','george@gmail.com','61489921018','Australia',113)
insert into Counsellor(Counsellor_Name,Contact_Email,Contact_Number,country,Counsellor_id) values ('John Lawrence','john@gmail.com','447893984627','United Kingdom',114)
insert into Counsellor(Counsellor_Name,Contact_Email,Contact_Number,country,Counsellor_id) values ('Alyssa Kutro','alyssa@gmail.com','13479466861','United States',115)
insert into Counsellor(Counsellor_Name,Contact_Email,Contact_Number,country,Counsellor_id) values ('Mehmet Sultan','mehmet@gmail.com','904388548628','Turkey',116)
select * from Counsellor
SET IDENTITY_INSERT Counsellor Off;
