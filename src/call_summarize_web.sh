# Set Pinecone API and Environment

export PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
export PINECONE_ENVIRONMENT="YOUR_PINECONE_ENVIRONMENT"
export PINECONE_INDEX_NAME="YOUR_PINECONE_INDEX"
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

# to be automated on process tweet later
python3 $HOME/src/webcrawling.py https://www.washingtonpost.com/national-security/2023/06/24/us-intelligence-prigozhin-putin/ > web.txt

python3 $HOME/src/showcase_pinecone.py

python3 $HOME/src/send_email2.py "Showcase Pinecone report" < $HOME/showcase_pinecone_output1.txt 
