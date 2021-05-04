from flask import render_template, redirect, url_for, request
from models import db, Project, app
import datetime


@app.route('/')
def index():
    all_projects = Project.query.all()
    return render_template('index.html', projects=all_projects)


@app.route('/about')
def about():
    all_projects = Project.query.all()
    return render_template('about.html', projects=all_projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def new():
    all_projects = Project.query.all()
    if request.form:
        new_project = Project(created=datetime.datetime.strptime(request.form['date'], "%Y-%m"),
                              title=request.form['title'],
                              description=request.form['desc'],
                              skills=request.form['skills'],
                              url=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=all_projects)


@app.route('/projects/<id>')
def detail(id):
    all_projects = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template('detail.html', projects=all_projects, project=project)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    all_projects = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        project.created = datetime.datetime.strptime(
            request.form['date'], "%Y-%m")
        project.title = request.form['title']
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.url = request.form['github']
        db.session.commit()
        print(project)
        return redirect(url_for('index'))
    return render_template('edit.html', projects=all_projects, project=project)


@app.route('/project/<id>/delete')
def delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", msg=error), 404


if __name__ == '__main__':
    db.create_all()
    project1 = Project(
        title="Number Guessing Game",
        created=datetime.datetime(2020, 3, 30),
        description="""
                    \nThis is a console game where you guess a number between 1 and 10. \
                    The job is to make a guess, and a players will get a message whether \
                    the guess is too high or too low. The next guess is based on the message. \
                    If the guess the right answer the game is done. Aim for the the lowest \
                    number of tries possible!
                    \n
                    \nHow to run the project locally:
                    \n
                    \nIf you have python installed, just run the `guessing_game.py`
                    \n
                    \nObjective:
                    \n
                    \nGuess a number 1-10 with the lowest number of tries.
                    \n
                    \nFlow:
                    \n
                    \n1. Guess a number between 1 and 10.
                    \n2. After every answer, a message is shown whether the guess is too high or too low.
                    \n3. If the guess is right, the game is done.
                    \n4. Player are asked if they want to play again.
                    \n
                    \nNotes:
                    \n
                    \n- Player inputs are validated(An int 1-10)
                    \n- At the start of each game, the current high score (least amount of points) is 
                    \rshown, so that players know what they're supposed to beat.""",
        skills="Creating a loop, Conditional statements, Accepting user input, Catching exceptions",
        url="https://github.com/bonanob/number_guessing_game")

    project2 = Project(
        title="Basketball Stats Tool",
        created=datetime.datetime(2020, 4, 7),
        description="""
                    \nThe app creates structures to store and organize a team of Basketball players into \
                    distributed teams. It will balance the teams by the total number of players, and also \
                    generate some statistics for a given team. Player data is imported from constants.py \
                    and is build into a structure of nested arrays.
                    \n
                    \nHow to run the project locally:
                    \n
                    \nIf you have python installed, have both .py files in a folder and run `app.py`
                    \n
                    \nObjective:
                    \n
                    \nDistribute players to teams so it's fair!
                    \n
                    \nFlow:
                    \n
                    \n1. User is prompted to see stats or quit.
                    \n2. User is prompted to choose a team.
                    \n3. Stats are shown.
                    \n4. User is prompted to redivide the teams(y/n)
                    \n
                    \n
                    \nNotes:
                    \n
                    \n- Players are redistributed every time you start or restart the app.""",
        skills="Importing data from files, Cleaning data, Building data structure using nested dictionaries, Validating user input",
        url="https://github.com/bonanob/team_distribution")

    project3 = Project(
        title="Number Guessing Game",
        created=datetime.datetime(2018, 6, 1),
        description="""
                    This is a console game  where you guess a number between 1 and 10. The job is to make a guess, and a players will get a message whether the guess is too high or too low. The next guess is based on the message. If the guess the right answer the game is done. Aim for the the lowest number of tries possible!
                    \n
                    \nHow to run the project locally:
                    \n
                    \nIf you have python installed, just run the `guessing_game.py`
                    \n
                    \nWhat I've learned:
                    \n
                    \n- Creating a loop
                    \n- Conditional statements
                    \n- Accepting user input
                    \n- Catching exceptions
                    \n
                    \nObjective:
                    \n
                    \nGuess a number 1-10 with the lowest number of tries.
                    \n
                    \nFlow:
                    \n
                    \n1. Guess a number between 1 and 10.
                    \n2. After every answer, a message is shown whether the guess is too high or too low.
                    \n3. If the guess is right, the game is done.
                    \n4. Player are asked if they want to play again.
                    \n
                    \nNotes:
                    \n
                    \n- Player inputs are validated(An int 1-10)
                    \n- At the start of each game, the current high score (least amount of points) is shown, so that players know what they're supposed to beat.""",
        skills="python",
        url="https://github.com/bonanob/number_guessing_game")

    project4 = Project(
        title="Number Guessing Game",
        created=datetime.datetime(2018, 6, 1),
        description="""
                    This is a console game  where you guess a number between 1 and 10. The job is to make a guess, and a players will get a message whether the guess is too high or too low. The next guess is based on the message. If the guess the right answer the game is done. Aim for the the lowest number of tries possible!
                    \n
                    \nHow to run the project locally:
                    \n
                    \nIf you have python installed, just run the `guessing_game.py`
                    \n
                    \nWhat I've learned:
                    \n
                    \n- Creating a loop
                    \n- Conditional statements
                    \n- Accepting user input
                    \n- Catching exceptions
                    \n
                    \nObjective:
                    \n
                    \nGuess a number 1-10 with the lowest number of tries.
                    \n
                    \nFlow:
                    \n
                    \n1. Guess a number between 1 and 10.
                    \n2. After every answer, a message is shown whether the guess is too high or too low.
                    \n3. If the guess is right, the game is done.
                    \n4. Player are asked if they want to play again.
                    \n
                    \nNotes:
                    \n
                    \n- Player inputs are validated(An int 1-10)
                    \n- At the start of each game, the current high score (least amount of points) is shown, so that players know what they're supposed to beat.""",
        skills="python",
        url="https://github.com/bonanob/number_guessing_game")

    # new_projects = [project1, project2]
    # db.session.add_all(new_projects)
    db.session.add(project1)
    db.session.commit()
    app.run(debug=True, port=8000, host='0.0.0.0')
