from flask import Flask, render_template, url_for, redirect
from forms import TeamForm, ProjectForm
from model import db, User, Team, Project, connect_to_db

app = Flask(__name__)

app.secret_key = "this is a secret key"

user_id = 1

@app.route("/")
def home():
    team_form = TeamForm()
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)
    return render_template("home.html", team_form = team_form, project_form=project_form)

@app.route("/add-team", methods=["POST"])
def add_team():
    team_form = TeamForm()

    if team_form.validate_on_submit():
        team_name = team_form.team_name.data
        new_team = Team(team_name, user_id)
        db.session.add(new_team)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@app.route("/add-project", methods=["POST"])
def add_project():
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)
    
    if project_form.validate_on_submit():
        project_name = project_form.project_name
        description = project_form.description.data
        completed = project_form.completed.data
        team_id = int(project_form.team_selection.data)
        print(project_name)
        type(project_name)

        new_project = Project(project_name, description, completed, team_id)
        
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)