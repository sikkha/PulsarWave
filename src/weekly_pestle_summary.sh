#!/bin/bash

#API Section
export OPENAI_API_KEY="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"


cd $HOME/PulsarWave/src
python3 $HOME/PulsarWave/src/final_process_tweet.py
python3 $HOME/PulsarWave/src/ai_weekly_pestle.py
python3 $HOME/PulsarWave/src/send_email2.py "Weekly Metageopolitical PESTLE" < /tmp/superb.txt

cp $HOME/PulsarWave/src/revised_accu_process_tweet.txt $HOME/PulsarWave/src/revised_accu_process_tweet.txt,orig
python3 $HOME/PulsarWave/src/trimmy_redundant_url.py $HOME/PulsarWave/src/revised_accu_process_tweet.txt,orig > $HOME/PulsarWave/trend-radar/docs/entry.txt
cd $HOME/PulsarWave/trend-radar/docs
$HOME/PulsarWave/trend-radar/docs/generate_trend_radar.sh