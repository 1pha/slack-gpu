import os
from typing import List

import requests
from flask import Flask, request, make_response
from dotenv import load_dotenv

from gpu import concat_msg


app = Flask(__name__)
load_dotenv(dotenv_path="..")


def fetch_gpu(ip: str) -> str:
    response = requests.get(url=f"https://{ip}.ngrok-free.app/return-status")
    msg = response.text
    return msg


@app.route('/gpu-webhook', methods=['POST'])
def gpu_webhook():
    if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        # Slack-API
        data = request.form
    elif request.headers['Content-Type'] == 'application/json':
        data = request.json
    else:
        print("error")

    ips: List[str] = os.getenv("SERVER_IPS").split(", ")
    msg = ""
    for ip in ips:
        msg = "\n".join([msg, fetch_gpu(ip=ip)])
    print("Success")
    return make_response(msg, 200, {"content_type": "application/json"})


@app.route('/return-status', methods=['GET'])
def return_status():
    msg = concat_msg()
    return make_response(msg, 200, {"content_type": "application/json"})


if __name__ == '__main__':
    app.run()
