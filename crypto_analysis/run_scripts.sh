#!/bin/bash
echo $(date +"%r")
echo "Starting run_script"
cd path/to/reddit-analysis/crypto_analysis/
echo "activating venv"
source venv/bin/activate

echo "getting tickers"
if python3 get_tickers.py ; then
    echo "running sentiment analysis"
    if python3 reddit_sentiment_analysis.py; then
        echo "sending email"
        if python3 send_email.py ; then
            echo "success"
        else
            echo "failed sending email :("
        fi
        echo "uploading to Google Cloud Storage"
        # only if you have permission ;)
        gsutil cp images/most_mentioned_picks_recent.png gs://reddit-analysis-812/crypto/
        gsutil cp images/sentiment_analysis_recent.png gs://reddit-analysis-812/crypto/
    else
        echo "failed reddit_sentiment_analysis :("
    fi
else
    echo "failed get_tickers :("
fi

echo "deactivating venv"
deactivate

echo "finished"