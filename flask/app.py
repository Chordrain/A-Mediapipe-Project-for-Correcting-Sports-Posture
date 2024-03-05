from flask import Flask, send_file

app = Flask(__name__)


@app.route("/mainpage-topbar-background")
def get_mainpage_topbar_background():
    return send_file('static/background1.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
