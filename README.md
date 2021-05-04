# Project 5: Portfolio with Flask-SQLAlchemy

This portfolio web application lets users list projects on the main page, and each project links to a detail page that displays the title, date, skills used, and description. Users can add or edit project information. When adding or editing a project, the application prompts the user for title, date, skills, description, and a link to a repo. The results for these entries are stored in a database and displayed on the homepage.

**How to run the project locally:**

1. Create a virtual environment
    - Mac: **`python3 -m venv env`**
    - Windows: **`python -m venv env`**
2. Activate your environment
    - Mac: **`source ./env/bin/activate`**
    - Windows: **`.\env\Scripts\activate`**
3. Install dependancies: **`pip install -r requirements.txt`**
4. Run the file **`app.py`**

**What I've learned:**

- Creating a model class and connecting it to db using Flask-SQLAlchemy
- Reading, updating, deleting with Flask-SQLAlchemy

- Creating Flask app
- Using template inheritance
- Using Form in Flask for user input

**Objective:** 

Create a web application to display projects.

**Routes for the Application:**

- **`/`** - Known as the root page, homepage, or landing page.
- **`/projects/new`** - The add new project route
- **`/projects/<id>`** - The view project detail route
- **`/projects/<id>/edit`** - The edit or update existing project route
- **`/projects/<id>/delete`** - Delete project route

**FLASK-SQLAlchemy Model:**

- **`Project`**
- Attributes: **`id`**(primary_key)**,  `title`**(string), **`description`**, **`skills`**, **`url`**(text) and **`date_updated`**(`datetime` object)

**Notes:**

- sqlite is used to create database.
- When editing existing projects fields are prepopulated with values.
- errorhandler(404) is Implemented .
