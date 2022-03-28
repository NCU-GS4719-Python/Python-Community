from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    a=1/0
    return 'Hello, Flask!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return '<h1>Hello, %s^^<h1>' % escape(username)

@app.route('/user')
def user_page():
    return '請在網址輸入名稱'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug= True)
