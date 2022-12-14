from flask import Flask, render_template
from forms import TeamForm

app = Flask(__name__)

@app.route("/")
def home():
    team_form = TeamForm()
    
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)