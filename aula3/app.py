from flask import Flask

app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<nome>') # Url dinâmica
def hello(nome=''):
    return f'Hello {nome}'


@app.route('/blog/')
@app.route('/blog/<int:id>') # Url dinâmica para inteiros
def blog(id=-1):
    if id >= 0:
        return f'Blog info {id}'
    else:
        return f'Blog todo'


if __name__ == '__main__':
    app.run()