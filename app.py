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
    app.run(debug=True, port=8000, host='127.0.0.1')
