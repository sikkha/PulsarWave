#!/bin/bash
source $HOME/.bashrc

#API Section
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"


# Read the file content
file_content=$(cat /tmp/select_tweet.txt)

# Check if the content contains "I don't know"
if [[ "$file_content" == *"I don't know"* ]]
then
    # Copy the content of /tmp/select_tweet_work.txt to /tmp/select_tweet.txt
    cp /tmp/select_tweet_work.txt /tmp/select_tweet.txt
fi

python3 $HOME/PulsarWave/src/from_select_tweet_to_json.py

python3 $HOME/PulsarWave/src/sixhour_ai.py > /tmp/sixhour_scan.txt

cp /tmp/select_tweet.txt /tmp/select_tweet_work.txt
