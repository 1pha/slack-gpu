import subprocess
import os

from dotenv import load_dotenv

from src.gpu import concat_msg


load_dotenv()


def send_msg(msg: str):
    webhook_url = os.getenv("WEBHOOK_URL")
    
    data = {"text": msg}
    data = str(data)
    subprocess.run(['curl', '-X', 'POST', '-H',
                    'Content-type: Application/json',
                    '--data', data, webhook_url])


if __name__=="__main__":
    msg = concat_msg()
    # print(msg)
    send_msg(msg=msg)