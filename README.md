# GNock-gnock
Send GPU status to slack server
1. Send GPU status on designated time
2. Get GPU status via slack command `/quota`

## 📤 Send GPU stats from Server to Slack

#### 1. ⚙️ Install

```bash
# Initialize
git clone https://github.com/Cognitive-Systems-Laboratory/slack-gpu
cd slack-gpu

# Install
chmod +x install.sh
conda create -n slack python=3.10 -y && conda activate slack # Optional
./install.sh

# Configuration File
touch .env
echo WEBHOOK_URL=(YOUR_WEBHOOK_URL_HERE) >> .env
```

#### 2. 📨 Send `nvidia-smi` result to Slack
```bash
python send.py
```

#### 3. ♻️ Spawn Jobs everyday

We will do this with `cron`

**Starting `cron`**
```bash
sudo apt update -y
sudo apt install -y cron
sudo service cron start
sudo systemctl enable cron.service
```

**Spawning Jobs on `cron`**
1. Make `run.sh` executable via `chmod +x run.sh`
2. Go to cron job batch file via `crontab -e`
3. Append the following
    ```bash
    0 9 * * * (PATH_HERE)/run.sh
    ```
    _Need to test if this cron is valid!_

**Misc.**
+ If somebody encountered `systemctel command not found`: Do `sudo apt-get install systemd`
+ Check if cron is running: `sudo service cron status`


## 📥 Query GPU stats from Slack to Server
I am running 3 GPU servers and one small personal server. The slack command `/quota` sends query to the personal server, and the personal server will send query to GPU servers to get the status.
- Slack (send `/quota` command) -> `POST https://(PERSONAL)/gpu-webhook` -> Invoke `GET https://(ith-GPU)/return-status` -> Concat Messages -> Return Message

#### 1. Middleware (personal server)

1. Setup `.env` file: This should include GPU servers' IP account. Split based on ", "
2. [Setup `ngrok`](https://dashboard.ngrok.com/get-started/setup/linux). Be aware of port.
3. Run flask app. No need to add `--host=0.0.0.0`, since we are using `ngrok`.
4. Test with POST command

#### 2. GPU Server Endpoint
1. Setup `ngrok`. Again, be aware of port.
2. Run flask app.

**Misc.**
- Starting with ngrok. Need personal authentication token for this.
    ```bash
    curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
  ngrok config add-authtoken (AUTHTOKEN)
  ngrok http http://localhost:5000
    ```

## Reference
+ [How to start with sending messages to your slack workspace from external sources](https://api.slack.com/apps/A062VRB6W7L/incoming-webhooks?success=1)
    - I'm using this `curl ...` command in this excercise. Just so you know. Convert this to `requests.get`
+ [Starting with Slack Slash-commands](https://api.slack.com/interactivity/slash-commands)

## TODO
[x] Receive send command from slacks so that the user can get a _current_ status of GPUs.
    - [Slash commands](https://api.slack.com/apps/A063KBUA5DE/slash-commands?)
[ ] Add test github actions.
[ ] Do the same thing for storages.
