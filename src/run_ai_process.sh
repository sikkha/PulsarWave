#!/bin/bash
source $HOME/.bashrc

#API Section
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

#twitter API series
# API keyws that yous saved earlier
export API_KEY="YOUR_TWITTER_API_KEY"
export API_SECRETS="YOUR_TWITTER_API_SECRETS"
export BEARER_TOKEN="YOUR_TWITTER_BEARER_TOKEN"
export ACCESS_TOKEN="YOUR_TWITTER_ACCESS_TOKEN"
export ACCESS_SECRET="YOUR_TWITTER_ACCESS_SECRET"


# Execute the Python script and redirect stdout and stderr
python3 $HOME/PulsarWave/src/ai_process_tweet.py 1> /tmp/j1.txt 2> /tmp/j2.txt

# Read the content of the file into a variable
tweet_content=$(cat /tmp/process_tweet.txt)

# Check the content of the variable
if [[ $tweet_content == *"I don't know"* ]]; then
    # If "I don't know" is found, re-run the Python script
    python3 $HOME/PulsarWave/src/ai_process_tweet.py 1> /tmp/j1.txt 2> /tmp/j2.txt
fi

cat /tmp/j1.txt >> $HOME/output2.txt
cat /tmp/process_tweet.txt >> $HOME/accu_process_tweet.txt
python3 $HOME/PulsarWave/src/send_email2.py "Your Processed Tweet" < /tmp/process_tweet.txt

