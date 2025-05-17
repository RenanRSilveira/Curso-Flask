from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'


def teste():
    return 'abc123'


app.add_url_rule('/teste', 'teste', teste) # Cria url


if __name__ == '__main__':
    app.run()