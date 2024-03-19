import os

from dotenv import load_dotenv

from src.gpu import concat_msg
from src.comm import send_msg


if __name__=="__main__":
    load_dotenv()
    webhook_url = os.getenv("WEBHOOK_URL")

    msg = concat_msg()
    send_msg(msg=msg, webhook_url=webhook_url)
