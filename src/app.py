import os
from typing import List

from flask import Flask, make_response
from dotenv import load_dotenv

import gpu
import comm


app = Flask(__name__)
load_dotenv(dotenv_path="..")


@app.route('/gpu-webhook', methods=['POST'])
def gpu_webhook():
    ips: List[str] = os.getenv("SERVER_IPS").split(", ")
    msg: str = comm.get_stats(ips=ips)
    print("Success")
    return make_response(msg, 200, {"content_type": "application/json"})


@app.route('/return-status', methods=['GET'])
def return_status():
    msg = gpu.concat_msg()
    return make_response(msg, 200, {"content_type": "application/json"})


if __name__ == '__main__':
    app.run()
