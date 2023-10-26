# GNock-gnock
Send GPU status to slack server

## Steps

#### 1. ⚙️ Setup 

```bash
# Initialize
git clone https://github.com/Cognitive-Systems-Laboratory/slack-gpu
cd slack-gpu

# Install
chmod +x install.sh
conda create -n slack python=3.10 -y && conda activate slack
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

## Reference
+ [How to start with sending messages to your slack workspace from external sources](https://api.slack.com/apps/A062VRB6W7L/incoming-webhooks?success=1)
    - I'm using this `curl ...` command in this excercise. Just so you know.