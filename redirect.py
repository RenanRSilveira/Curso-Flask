from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/login')
def login():
    return f'Bem-vindo à página de login'


@app.route('/nome-aleatorio')
def redirecionar(): # será redirecionado para a página /login
    return redirect(url_for('login'))# o url_for tira a /


if __name__ == '__main__':
    app.run()
