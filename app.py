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
        print(new_project)
        db.session.add(new_project)
        db.session.commit()
    return render_template('projectform.html', projects=all_projects)


@app.route('/projects/<id>')
def detail(id):
    all_projects = Project.query.all()
    project = Project.query.get(id)
    return render_template('detail.html', projects=all_projects, project=project)


@app.route('/projects/<id>/edit')
def edit(id):
    all_projects = Project.query.all()
    return render_template('index.html', projects=all_projects)


@app.route('/project/<id>/delete')
def delete(id):
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", msg=error), 404


if __name__ == '__main__':
    db.create_all()
    project1 = Project(title="Number Guessing Game",
                       description="""
                            Objective: Guess a number 1-10 with the lowest number of tries.<br>
                            
                            Process:<br>
                            Guess a number between 1 and 10.
                            After every answer, a message is shown whether the guess is too high or too low.
                            If the guess is right, the game is done.\n\n\n
                            Player are asked if they want to play again.\n\n\n
                            
                            Notes:\n
                            Player inputs are validated(An int 1-10)
                            At the start of each game, the current high score (least amount of points) is shown, so that players know what they're supposed to beat.""",
                       skills="python",
                       url="https://github.com/bonanob/number_guessing_game")
    new_projects = [project1, project1]
    db.session.add_all(new_projects)
    db.session.commit()
    app.run(debug=True, port=8000, host='127.0.0.1')
