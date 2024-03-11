from flask import Flask, send_file, send_from_directory

app = Flask(__name__, static_folder='static')


@app.route("/")
def hello_world():
    return "hello world"


@app.route("/mainpage-topbar-background")
def get_mainpage_topbar_background():
    return send_file('static/background1.png', mimetype='image/png')


@app.route("/static/<path:filename>")
def get_app_icon(filename):
    return send_from_directory(app.static_folder, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
