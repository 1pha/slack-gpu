import os
from dotenv import load_dotenv

import gpu
import comm


load_dotenv(dotenv_path="..")


def test_concat_msg():
    print("Test `test_concat_msg`")
    msg = gpu.concat_msg()
    print(msg)
    assert msg, f"Message is null: {msg}"


def test_comm():
    print("Test `test_comm`")
    ips = os.getenv("SERVER_IPS").split(", ")
    msg = comm.get_stats(ips=ips)
    print(msg)
    assert msg, f"Message from GPU servers is null: {msg}"
    
    
def test_comm_fail():
    """Intentionally send query to wrong servers"""
    ips = os.getenv("WRONG_IPS").split(", ")
    msg = comm.get_stats(ips=ips)
    assert msg == "", f"Message from GPU should be null: {msg}"
