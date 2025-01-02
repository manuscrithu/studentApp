# Student App

The **Student App** is a Django-based web application designed to manage student records. It allows users to perform CRUD (Create, Read, Update, Delete) operations on student data such as **Name**, **NIC** (National Identification Number), and **Resident**. This application also includes search functionality to filter students based on these fields.

## Features

- **View All Students**: Display a list of all students in the database.
- **Add New Student**: Form for adding new student details to the system.
- **View Individual Student**: Display details of a single student.
- **Update Student**: Modify an existing student's details.
- **Delete Student**: Remove a student from the database.
- **Search Students**: Filter students by NIC, Name, or Resident.

## Installation

### 1. Clone the Repository

```bash```
git clone https://github.com/yourusername/student-app.git
2. Set Up a Virtual Environment
Ensure you have Python installed. Then create a virtual environment to manage your project's dependencies:

```bash```
cd student-app
python -m venv .venv
source .venv/bin/activate  # For Mac/Linux
.venv\Scripts\activate  # For Windows
3. Install Dependencies
Install the required Python packages listed in requirements.txt:

```bash```
pip install -r requirements.txt
4. Configure Database
The application uses an SQLite database by default. You can switch to another database system by modifying the DATABASES setting in settings.py.

5. Run Migrations
Create the necessary database tables:

```bash```
python manage.py migrate
6. Create Superuser (Optional)
Create an admin user to access the Django admin interface:

```bash```
python manage.py createsuperuser
7. Run the Development Server
Start the Django development server:

```bash```
python manage.py runserver
You can now access the app by navigating to http://127.0.0.1:8000/ in your web browser.

URL Structure
Home Page: / - Displays a list of all students.
Add Student: /add/ - Form to add a new student.
View Student: /app/<nic>/ - View details of a single student.
Update Student: /app/<nic>/update/ - Form to update student details.
Delete Student: /app/<nic>/delete/ - Confirm and delete a student record.
Search Students: /search/ - Filter students by NIC, Name, or Resident.
Templates
app.html: Displays all students in a list.
datain.html: Form for adding a new student.
child.html: Displays detailed information about a student.
update.html: Form to update an existing student's details.
confirm_delete.html: Confirmation page before deleting a student.
Contributing
If you would like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are always welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Django Framework: For building the web application.
SQLite: For the database used in this project.
HTML/CSS: For creating the user interface.
