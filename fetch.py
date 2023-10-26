import subprocess
import os

from dotenv import load_dotenv

from src.gpus import showUtilization


load_dotenv()


def get_nvidia_smi() -> str:
    # Run nvidia-smi and capture the output
    result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, text=True)
    nvidia_smi_output = result.stdout

    # Print the output (for testing purposes)
    return nvidia_smi_output
    

def get_gputil() -> str:
    msg = showUtilization(all=True, useOldCode=True)
    return msg


def get_server() -> str:
    # Get Server name
    # Note that server name should be saved as environment variable as `SERVER_NAME`
    server_name = subprocess.run(['curl', 'ifconfig.me'],
                                stdout=subprocess.PIPE, text=True)
    server_name = server_name.stdout
    server_name = f"Server IP: {server_name}"
    return server_name


def concat_msg() -> str:
    server_msg = get_server()
    gpu_msg = get_gputil()
    
    msg = f"{server_msg}\n{gpu_msg}"
    return msg


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