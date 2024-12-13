from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', title='Home')

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)