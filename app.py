from os import getenv as env
from flask import Flask, jsonify, request
from requests import get as GET

app = Flask(__name__)


@app.route("/")
def root():
    username = request.args.get("username")
    client_id = env("CLIENT_ID")
    client_secret = env("CLIENT_SECRET")
    url = f"https://api.github.com/users/{username}"
    r_args = f"?client_id={client_id}&client_secret={client_secret}"
    try:
        r = GET(url + r_args)
    except:
        r = "<i>Request Failed: Please try again after 2 minutes.</i>"
    response = app.response_class(
        response=r,
        status=200,
        mimetype="application/json"
    )
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
