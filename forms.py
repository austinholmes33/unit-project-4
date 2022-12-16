from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length


class TeamForm(FlaskForm):
    team_name = StringField("Team name", validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("Submit")

class ProjectForm(FlaskForm):
    project_name = StringField("Project name", validators=[DataRequired(), Length(min=4, max=255)])
    description = StringField("Description")
    completed = BooleanField("Completed?")
    team_selection = SelectField("Team")
    submit = SubmitField("Submit")

    def update_teams(self, teams):
        self.team_selection.choices = [ (team.id, team.team_name) for team in teams]