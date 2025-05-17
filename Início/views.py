from main import app
from flask import render_template


# rotas
@app.route("/")
def homepage():
    return render_template('homepage.html')


@app.route("/receita")
def blog():
    return render_template('receita.html')


