from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/example')
def example_route():
    my_list = [1, 2, 3, 4, 5]
    return jsonify({'my_list': my_list})

if __name__ == '__main__':
    app.run(debug=True)
