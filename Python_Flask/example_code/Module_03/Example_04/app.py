from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    # 註解掉下面一行就會出現程式錯誤
    # a=1/0
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('user.html', username = username)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)
