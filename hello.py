from flask import Flask, url_for,request,render_template
from markupsafe import escape
app = Flask(__name__)
import numpy as np

@app.route('/')
def hello_world():
    return 'Hello,World!'

#input = np.array()
#@app.route('.',methods=['POST'])
#def predict():


@app.route('/user/<user_name>')
def show_user_profile(user_name):
    return 'User %s'  % escape(user_name)

@app.route('/post/<int:post_id>')
def show_post (post_id):
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('show_post', post_id = '20'))
    print(url_for('static', filename='test.py'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return hello_world()
    else:
        return projects()

@app.route('/index')
def index():
    user = {'username':'Shellz'}
    return render_template('index.html',user=user)

if __name__ == '__main__':
    app.run(debug=True)