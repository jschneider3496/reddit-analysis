# reddit-analysis
See Bitcamp 2021 submission for information: https://devpost.com/software/reddit-crypto-analysis. Project hosted [here](https://jschneider3496.github.io/reddit-analysis/webpage/index.html)

## How to use

### Prerequisite
* Linux/Unix (was developed/tested on Raspberry Pi)
* [Python 3](https://www.python.org/downloads/)
* [Pip and venv] (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
* [NLTK] (https://www.nltk.org/install.html)
* [Google Cloud SDK] (https://cloud.google.com/sdk/docs/install) (optional)
* Google Cloud Storage bucket (optional)

### Code Changes
* In reddit-analysis/crypto_analysis/reddit_sentiment_analysis.py, you need to add reddit praw credentials. See [this](https://pythonprogramming.net/introduction-python-reddit-api-wrapper-praw-tutorial/) for help.
* In reddit-analysis/crypto_analysis/send_email.py, you need to add a sender and receiver. For Gmail, make sure that sender has "Less secure app access" turned ON.
* In reddit-analysis/crypto_analysis/run_scripts.sh, you need to update the path to your script. You also want to update/remove the Google Cloud Storage upload.
* In reddit-analysis/webpage/index.html, you may want to update the image src to reflect your image location.

### Install & Run
```bash
git clone https://github.com/jschneider3496/reddit-analysis.git
cd reddit-analysis/crypto_analysis
source venv/bin/activate
pip install -r requirements.txt
./run_scripts.sh
```

### Automation
If on Raspberry Pi (or other Unix-like computers), create a time-based job to run the script periodically with cron.
* [Cron Raspberry Pi tutorial](https://www.raspberrypi.org/documentation/linux/usage/cron.md)
* ```0 * * * * /path/to/reddit-analysis/crypto_analysis/run_scripts.sh```
