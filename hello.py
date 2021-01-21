
from flask import Flask

app = Flask(__name__)
"""
To start the hello.py application from the previous section, first make sure the virtual environment you created earlier is activated and has Flask installed in it. For Linux and macOS users, start the web server as follows:
(venv) $ export FLASK_APP=hello.py (venv) $ flask run
* Serving Flask app "hello"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
"""

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

##Dynamic Routes
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)



if __name__ == '__main__': app.run()