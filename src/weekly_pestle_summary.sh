#!/bin/bash

#API Section
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"


python3 $HOME/PulsarWave/src/final_process_tweet.py 
python3 $HOME/PulsarWave/src/ai_weekly_pestle.py
python3 $HOME/PulsarWave/src/send_email2.py "Weekly Metageopolitical PESTLE" < /tmp/superb.txt

cp $HOME/revised_accu_process_tweet.txt $HOME/PulsarWave/trend-radar/docs/entry.txt
cd $HOME/PulsarWave/docs
$HOME/PulsarWave/trend-radar/docs/generate_trendradar.sh
