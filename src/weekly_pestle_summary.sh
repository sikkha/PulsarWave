#!/bin/bash

#API Section
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"


python3 $HOME/final_process_tweet.py 
python3 $HOME/ai_weekly_pestle.py
python3 $HOME/send_email2.py "Weekly Metageopolitical PESTLE" < /tmp/superb.txt

