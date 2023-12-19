# Importing essential modules
import typing
from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc
import re


# Replace these with your own database connection details
server = 'DESKTOP-G4BD51J'
database = 'uniengine'  # Name of your Northwind database     
use_windows_authentication = False  # Set to True to use Windows Authentication
username = 'sa'  # Specify a username if not using Windows Authentication
password = 'ashbah123'  # Specify a password if not using Windows Authentication

# Create the connection string based on the authentication method chosen
if use_windows_authentication:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
else:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Main Window Class
class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes _init_ method
        super(UI, self).__init__()

        # Load the .ui file
        uic.loadUi('GUI_Elements/Choose_Option.ui', self)
        self.show()
        self.adminButton.clicked.connect(self.openadminlogin)
        self.studentButton.clicked.connect(self.openstudentlogin)

    def openadminlogin(self):
        self.close()
        self.admin_login = AdminLogin()
        self.admin_login.show()
    
    def openstudentlogin(self):
        self.close()
        self.student_login= StudentLogin()
        self.student_login.show()


#++++++++++++++++++++++++this class is for Admin Login Page++++++++++++++++++++++++
class AdminLogin(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(AdminLogin, self).__init__()
        # Load the .ui file
        uic.loadUi('GUI_Elements/Admin Login.ui', self)
        self.adminloginButton.clicked.connect(self.login)
        self.adminregisterButton.clicked.connect(self.registerAdmin) #if register button clicked
        self.backbutton.clicked.connect(self.backscreen)
        
    
    #when regiser button clicked new admin's entered email and password will then be added to the database of admin
    def registerAdmin(self):
        new_email=self.adminEmail.text()
        new_password=self.adminPassword.text()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            QtWidgets.QMessageBox.warning(self, "Invalid Email", "Please enter a valid email address.")
            return

        connection=pyodbc.connect(connection_string)
        cursor=connection.cursor()
        query="select * from Administrator where Admin_Email=? and Admin_Password=?"   
        cursor.execute(query,(new_email,new_password))
        row=cursor.fetchone()
        if new_email!="" and new_password!="":
            if row is None:
                query_insert = "INSERT INTO Administrator (Admin_Email, Admin_Password) VALUES (?, ?)"  
                cursor.execute(query_insert, (new_email, new_password))
                connection.commit()
                #again searching database to extract new admin id
                query="select * from Administrator where Admin_Email=? and Admin_Password=?"   
                cursor.execute(query,(new_email,new_password))
                row=cursor.fetchone()
                new_adminID=row[0]
                print(new_adminID,"newadmin registered")
                QtWidgets.QMessageBox.information(self, "Confirm Email", "Verify your email!")
                self.close()
                self.add_uni= AddUniversity(new_adminID)
                self.add_uni.show()
                
            else:
                QtWidgets.QMessageBox.information(self, "Sign Up Failed", "This user already exists")
        else:
            QtWidgets.QMessageBox.warning(self, "Registration Failed", "Enter your Email Address and Password")

    def login(self):
        email=self.adminEmail.text()
        password=self.adminPassword.text()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            QtWidgets.QMessageBox.warning(self, "Invalid Email", "Please enter a valid email address.")
            return
        connection=pyodbc.connect(connection_string)
        cursor=connection.cursor()

        query="select * from Administrator where Admin_Email=? and Admin_Password=?"  
        cursor.execute(query,(email,password))
        row=cursor.fetchone()
        if row:
            Admin_Id=row[0]
            print(Admin_Id,"ss")
            self.open_AdminDashboard(Admin_Id)
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid Email or Password. Please try again. If you've never registered before then enter email and password then click Regiser Button")

    def open_AdminDashboard(self,Admin_Id):
        self.close()
        print(Admin_Id,"ssssdash")
        self.admin_dashboard= AdminDashboard(Admin_Id)
        self.admin_dashboard.show()
    def backscreen(self):
        self.close()
        self.back= UI()
        self.back.show()


#++++++++++++++++++++++++this class is for Admin Dashboard++++++++++++++++++++++++
class AdminDashboard(QtWidgets.QMainWindow):
    def __init__(self, Admin_Id):
        print(Admin_Id,"dashboard")
        # Call the inherited classes __init__ method
        super(AdminDashboard, self).__init__()
        # Load the .ui file
        uic.loadUi('GUI_Elements/Admin Dashboard.ui', self)
        self.display_university_data(Admin_Id)
        self.editNowButton.clicked.connect(lambda:self.edit(Admin_Id))
        self.backbutton.clicked.connect(self.backscreen)

    def display_university_data(self,Admin_Id):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Example query to fetch university data
        query = "SELECT * FROM University where Admin_Id=?"
        cursor.execute(query,(Admin_Id))
        row=cursor.fetchone()
        #self.editNowButton.clicked.connect(self.edit)
        if row:
            self.UniName.setText(str(row[1]))
            self.UniCity.setText(str(row[2]))
            self.UniCountry.setText(str(row[3]))
            self.UniType.setText(str(row[8]))
            self.UniTest.setText(str(row[4]))
            self.UniSAT.setText(str(row[6]))
            self.UniAvgCost.setText(str(row[7]))


    def edit(self,Admin_Id):#changed 1
        self.close()
        print(Admin_Id,"hi")
        self.edit_uni= EditUniversityDetails(Admin_Id)#changed 1
        self.edit_uni.show()
    def backscreen(self):
        self.close()
        self.back= AdminLogin()
        self.back.show()

#++++++++++++++++++++++++this is class for Edit University ++++++++++++++++++++++++
class EditUniversityDetails(QtWidgets.QMainWindow):
    def __init__(self,Admin_Id):#changed 1
        # Call the inherited classes __init__ method
        super(EditUniversityDetails, self).__init__()
        # Load the .ui file
        uic.loadUi('GUI_Elements/Edit University Details (Login Now) - By Administrator.ui', self)

        #CHANGES DONE FROM HERE 

        self.pushButton_2.clicked.connect(lambda:self.editUni(Admin_Id))
        self.backbutton.clicked.connect(lambda:self.backscreen(Admin_Id))

        
    def editUni(self,Admin_Id):
        print(Admin_Id)
        new_university_name = self.UniName.text()
        new_uni_city=self.UniCity.text()
        new_uni_country=self.UniCountry.text()
        new_uni_type=self.UniType.text()
        new_uni_entry=self.UniTest.text()
        new_uni_rate=self.UniRate.text()
        new_uni_sat=self.UniSAT.text()
        new_uni_cost=self.UniAvgCost.text()


        if new_university_name:
            # Connect to the database
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            

            # Example query to update university name
            update_query = """UPDATE University 
                            SET University_Name = ? where Admin_ID=?"""
            cursor.execute(update_query, new_university_name,Admin_Id)


            # Commit the changes to the database
            connection.commit()

            # Close the connection
            connection.close()
        if new_uni_city:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()


            # Example query to update university name
            update_query = """UPDATE University 
                            SET University_City = ? where Admin_ID=?"""
            cursor.execute(update_query, new_uni_city,Admin_Id)


            # Commit the changes to the database
            connection.commit()

            # Close the connection
            connection.close()
        if new_uni_country:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            # Example query to update university name
            update_query = """UPDATE University 
                            SET University_Country = ? where Admin_ID=?"""
            cursor.execute(update_query,new_uni_country,Admin_Id)


            # Commit the changes to the database
            connection.commit()

            # Close the connection
            connection.close()
        if new_uni_type:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            # Example query to update university name
            update_query = """UPDATE University 
                            SET University_Type = ? where Admin_ID=?"""
            cursor.execute(update_query,new_uni_type,Admin_Id)


            # Commit the changes to the database
            connection.commit()

            # Close the connection
            connection.close()
        if new_uni_entry:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            # Example query to update university name
            update_query = """UPDATE University 
                            SET Entry_Test= ? where Admin_ID=?"""
            cursor.execute(update_query,new_uni_entry,Admin_Id)


            # Commit the changes to the database
            connection.commit()

            # Close the connection
            connection.close()
    
        if new_uni_rate:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            # Example query to update university name
            update_query = """UPDATE University 
                            SET Acceptance_Rate= ? where Admin_ID=?"""
            cursor.execute(update_query,new_uni_rate,Admin_Id)


            # Commit the changes to the database
            connection.commit()

            # Close the connection
            connection.close()

        if new_uni_sat:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            # Example query to update university name
            update_query = """UPDATE University 
                            SET SAT_score= ? where Admin_ID=?"""
            cursor.execute(update_query,new_uni_sat,Admin_Id)


            # Commit the changes to the database
            connection.commit()

            # Close the connection
            connection.close()

        if new_uni_cost:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            # Example query to update university name
            update_query = """UPDATE University 
                            SET Avg_Annual_Cost= ? where Admin_ID=?"""
            cursor.execute(update_query,new_uni_cost,Admin_Id)


            # Commit the changes to the database
            connection.commit()

            # Close the connection
            connection.close()
        

        self.close()
    def backscreen(self,Admin_Id):
        self.close()
        self.back= AdminDashboard(Admin_Id)
        self.back.show()
       

#++++++++++++++++++++++++this is class Add University++++++++++++++++++++++++
class AddUniversity(QtWidgets.QMainWindow):
    def __init__(self,new_adminID):
        print(new_adminID,"newAdmin uni")
        # Call the inherited classes __init__ method
        super(AddUniversity, self).__init__()
        # Load the .ui file
        uic.loadUi('GUI_Elements/Add University Details (Register Now) - By Administrator.ui', self)
        self.addsubmit_button.clicked.connect(lambda:self.insertUni(new_adminID))
        self.backbutton.clicked.connect(self.backscreen)

    def insertUni(self,new_adminID):
        uni_name=self.UniName.text()
        uni_city=self.UniCity.text()
        uni_country=self.UniCountry.text()
        uni_type=self.UniType.text()
        uni_test=self.UniTest.text()
        uni_accept=self.UniAccept.text()
        uni_sat=self.UniSAT.text()
        uni_cost=self.UniCost.text()
        connection=pyodbc.connect(connection_string)
        cursor=connection.cursor()
        query="INSERT INTO University (University_Name,University_City,University_Country,Entry_Test,Acceptance_Rate,SAT_score,Avg_Annual_Cost,University_Type,Admin_ID) VALUES (?, ?,?,?,?,?,?,?,?)"   
        cursor.execute(query,(uni_name,uni_city,uni_country,uni_test,uni_accept,uni_sat,uni_cost,uni_type,new_adminID))
        connection.commit()
        self.close()
    def backscreen(self):
        self.close()
        self.back= AdminLogin()
        self.back.show()
        

#++++++++++++++++++++++++this is class Student Login++++++++++++++++++++++++
class StudentLogin(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(StudentLogin, self).__init__()
        # Load the .ui file
        uic.loadUi('GUI_Elements/Student Login.ui', self)
        self.studentLoginbutton.clicked.connect(self.loginStudent)
        self.studentSignUpButton.clicked.connect(self.signupStudent)
        self.backbutton.clicked.connect(self.backscreen)

    def loginStudent(self):
        
        stdent_email = self.studentEmail.text()
        student_password = self.studentPassword.text()

        # Check if email follows the pattern of having @ and .com
        if not re.match(r"[^@]+@[^@]+\.[^@]+", stdent_email):
            QtWidgets.QMessageBox.warning(self, "Invalid Email", "Please enter a valid email address.")
            return

        # Check if @ appears only once and not at the beginning or end
        if stdent_email.count('@') != 1 or stdent_email.startswith('@') or stdent_email.endswith('@'):
            QtWidgets.QMessageBox.warning(self, "Invalid Email", "Please enter a valid email address.")
            return

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "select * from Students where Student_Email=? and Student_Password=?"  
        cursor.execute(query, (stdent_email, student_password))
        row = cursor.fetchone()

        if row:
            self.open_StudentDashboard()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid Email or Password. Please try again. If you've never registered before then enter email and password then click Register Button")
    
    def signupStudent(self):
        self.close()
        self.signup_student= StudentRegister()
        self.signup_student.show()


    def open_StudentDashboard(self):
        self.close()
        self.student_dashboard= StudentDashboard()
        self.student_dashboard.show()

    def backscreen(self):
        self.close()
        self.back= UI()
        self.back.show()


#++++++++++++++++++++++++this is class Student Dashboard++++++++++++++++++++++++
class StudentDashboard(QtWidgets.QMainWindow):
    def __init__(self):
        #print(Student_Id,"Student ID - Std Dash")
        # Call the inherited classes __init__ method
        super(StudentDashboard, self).__init__()
        # Load the .ui file
        uic.loadUi('GUI_Elements/Student Dashboard.ui', self)
        self.searchButton.clicked.connect(self.open_SearchUni)
        self.councellorButton.clicked.connect(self.open_searchCounsellor)
        self.backbutton.clicked.connect(self.backscreen)

    def open_SearchUni(self):
        self.close()
        self.uni_search=SearchUniversity()
        self.uni_search.show()

    def open_searchCounsellor(self):
        self.close()
        self.couns_search=SearchCounsellor()
        self.couns_search.show()
    def backscreen(self):
        self.close()
        self.back= StudentLogin()
        self.back.show()

#++++++++++++++++++++++++this is class Student Uni Search++++++++++++++++++++++++
class SearchUniversity(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(SearchUniversity, self).__init__()
        # Load the .ui file
        uic.loadUi('GUI_Elements/Search University - By Student.ui', self)
        self.searchtoPop.clicked.connect(self.populateSearchtable)
        self.viewButton.clicked.connect(self.open_Universitydisplay)
        self.backbutton.clicked.connect(self.backscreen)
    
    def populateSearchtable(self):
        while (self.UnitabletableWidget.rowCount() > 0):
        
            self.UnitabletableWidget.removeRow(0)
        
        uni_name = self.searchbyname.text()
        uni_country = self.UniCountry.text()
        uni_city = self.UniCity.text()
        Uni_type = self.UniType.text()
        sat_score = self.satScore.text()
        acceptance = self.acceptanceRate.text()

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query_params = []

        query = "SELECT * FROM University WHERE"

        if uni_name:
            query += " University_Name LIKE ? AND"
            query_params.append(f'%{uni_name}%')

        if uni_city:
            query += " University_City LIKE ? AND"
            query_params.append(f'%{uni_city}%')

        if uni_country:
            query += " University_Country LIKE ? AND"
            query_params.append(f'%{uni_country}%')

        if Uni_type:
            query += " University_Type LIKE ? AND"
            query_params.append(f'%{Uni_type}%')

        if sat_score:
            query += " (SAT_score >= ? - 200  ) AND"
            query_params.extend([sat_score])

        if acceptance:
            query += " (Acceptance_Rate >= ? ) AND"
            query_params.extend([acceptance]) 


        # Remove the trailing 'AND' if there are conditions
        if len(query_params) > 0:
           query = query[:-3]
        

        cursor.execute(query, tuple(query_params))

        for row_index, row_data in enumerate(cursor.fetchall()):
            print(row_data)

            self.UnitabletableWidget.insertRow(row_index)
            item = QTableWidgetItem(str(row_data[1]))
            self.UnitabletableWidget.setItem(row_index, 0, item)





    def open_Universitydisplay(self):
        x = 5
        selected_items = self.UnitabletableWidget.selectedItems()

        if len(selected_items) > 0:
            selected_item = selected_items[0]
            selected_row = selected_item.row()

            # Get all items in the selected row
            row_items = []
            for col in range(self.UnitabletableWidget.columnCount()):
                item = self.UnitabletableWidget.item(selected_row, col)
                if item is not None:
                    row_items.append(item.text())
            #print(row_items)
            universityid=row_items[0]
            self.close()
            self.admin_dashboard= StudentUniversityDisplay(universityid)
            self.admin_dashboard.show()
        else:
             QtWidgets.QMessageBox.warning(self, "Item Error", "No item selected")
        
    def backscreen(self):
        self.close()
        self.back= StudentDashboard()
        self.back.show()

#++++++++++++++++++++++++this is class Student Uni Search Display++++++++++++++++++++++++
class StudentUniversityDisplay(QtWidgets.QMainWindow):
    def __init__(self,universityid):
        # Call the inherited classes __init__ method
        self.Unoversityid=universityid
        super(StudentUniversityDisplay, self).__init__()
        # Load the .ui file
        uic.loadUi('GUI_Elements\Display University - To Student.ui', self)
        self.display_university_data_student(universityid)
        self.backbutton.clicked.connect(self.backscreen)
    
    def display_university_data_student(self,universityid):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Example query to fetch university data
        query = "SELECT * FROM University where University_Name=?"
        cursor.execute(query,(universityid,))
        row=cursor.fetchone()
        #self.editNowButton.clicked.connect(self.edit)
    
        if row:
            self.UniName.setText(str(row[1]))
            self.UniCity.setText(str(row[2]))
            self.UniCountry.setText(str(row[3]))
            self.UniType.setText(str(row[8]))
            self.UniEntry.setText(str(row[4]))
            self.UniSAT.setText(str(row[6]))
            self.UniAvgCost.setText(str(row[7]))
            self.UniRate.setText(str(row[5]))
    def backscreen(self):
        self.close()
        self.back= SearchUniversity()
        self.back.show()

#++++++++++++++++++++++++this is class Student Register++++++++++++++++++++++++
class StudentRegister(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(StudentRegister, self).__init__()
        # Load the .ui file
        uic.loadUi('GUI_Elements/Register Now - By Student.ui', self)
        self.studentRegister.clicked.connect(self.registerStudent)
        self.backbutton.clicked.connect(self.backscreen)
    
    def registerStudent(self):
        full_name=self.namelabel.text()
        student_email=self.stdemail.text()
        student_pass=self.stdpass.text()
        student_confirm_pass=self.stdpasscon.text()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", student_email):
            QtWidgets.QMessageBox.warning(self, "Invalid Email", "Please enter a valid email address.")
            return
        connection=pyodbc.connect(connection_string)
        cursor=connection.cursor()
        query="select * from Students where Student_Email=? and Student_Password=? and Student_Name=?"   
        cursor.execute(query,(student_email,student_pass,full_name))
        row=cursor.fetchone()
        if row is None:
            if student_pass==student_confirm_pass:
                query_insert = "INSERT INTO Students (Student_Email, Student_Password,Student_Name) VALUES (?, ?, ?)"  
                cursor.execute(query_insert, (student_email, student_pass,full_name))
                connection.commit()
                QtWidgets.QMessageBox.information(self, "Confirm Email", "Verify your email!")
                self.close()
                self.stdDash= StudentDashboard()
                self.stdDash.show()
            else:
                QtWidgets.QMessageBox.warning(self, "Sign Up Failed", "Please make sure your passwords match. Please Try Again!")
        else:
            QtWidgets.QMessageBox.information(self, "Sign Up Failed", "This user already exists")
    def backscreen(self):
        self.close()
        self.back= StudentLogin()
        self.back.show()

#++++++++++++++++++++++++this is class to display counsellor++++++++++++++++++++++++
class SearchCounsellor(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(SearchCounsellor, self).__init__()
        # Load the .ui file
        uic.loadUi('GUI_Elements\Counsellors.ui', self)
        self.searhButton.clicked.connect(self.counsellorsearching)
        self.backbutton.clicked.connect(self.backscreen)

    def counsellorsearching(self):
        while (self.counsellorWidget.rowCount() > 0):
        
            self.counsellorWidget.removeRow(0)
        university_country=self.country.text()
        connection=pyodbc.connect(connection_string)
        cursor=connection.cursor()
        query="select * from  Counsellor where country like ?"

        cursor.execute(query,(f'%{university_country}%'))
   
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.counsellorWidget.insertRow(row_index)
        
        # Iterate through columns and insert items
            for col_index, col_value in enumerate(row_data):
                item = QTableWidgetItem(str(col_value))
                self.counsellorWidget.setItem(row_index, col_index, item)
    def backscreen(self):
        self.close()
        self.back= StudentDashboard()
        self.back.show()

def main():
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()