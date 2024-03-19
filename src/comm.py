import json
from typing import List

import requests


def send_msg(msg: str, webhook_url: str) -> int:
    data = json.dumps({"text": msg})
    response = requests.post(url=webhook_url, data=data,
                             headers={"Contenty-Type": "application/json"})
    status_code: int = response.status_code
    return status_code


def fetch_gpu(ip: str) -> str:
    response = requests.get(url=f"https://{ip}.ngrok-free.app/return-status")
    if response.status_code == 200:
        msg = response.text
    else:
        msg = ""
    return msg


def get_stats(ips: List[str]) -> str:
    msg = ""
    for ip in ips:
        _msg = fetch_gpu(ip=ip)
        if _msg:
            msg = "\n".join([msg, _msg])
    return msg
