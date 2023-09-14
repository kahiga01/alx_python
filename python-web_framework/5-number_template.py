#!/usr/bin/python3
"""a script that starts a Flask web application:
"""from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return "C {}".format(text)

@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return "Python {}".format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    if isinstance(n, int):
        return "{} is a number".format(n)
    else:
        return "Not a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('number_template.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

