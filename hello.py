from flask import Flask, render_template


app = Flask(__name__)
"""
To start the hello.py application from the previous section, first make sure the virtual environment you created earlier is activated and has Flask installed in it. For Linux and macOS users, start the web server as follows:
(venv) $ export FLASK_APP=hello.py (venv) $ flask run
* Serving Flask app "hello"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
"""

@app.route('/')
def index():
    return render_template('index.html')

# ##Dynamic Routes### The application will respond with the personalized greeting using the name dynamic argument. 
@app.route('/user/<name>')
def user(name):
    return render_template('user.html, name=name')



if __name__ == '__main__': app.run()