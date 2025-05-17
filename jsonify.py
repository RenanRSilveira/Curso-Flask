from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home'


@app.route('/api/dados')
def api_dados():
    data = {
        'nome': 'Renan',
        'idade': 23
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
