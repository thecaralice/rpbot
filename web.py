from flask import Flask
import git

app = Flask(__name__)
repo = git.Repo()


@app.route("/")
def main():
    return "Bot is alive!"


@app.route("/github")
def github():
    repo.remote().pull()
    return "", 204


def run():
    return app.run(host="0.0.0.0")
