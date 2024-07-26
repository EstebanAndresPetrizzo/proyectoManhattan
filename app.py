from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/services.html')
def services():
    return render_template('services.html')


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"key": "value"}
    return jsonify(data)


@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    return jsonify(new_data), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
