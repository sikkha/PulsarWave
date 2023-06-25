# Set Pinecone API and Environment

export PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
export PINECONE_ENVIRONMENT="YOUR_PINECONE_ENVIRONMENT"
export PINECONE_INDEX_NAME="YOUR_PINECONE_INDEX"
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

python3 webcrawling.py https://www.washingtonpost.com/national-security/2023/06/24/us-intelligence-prigozhin-putin/ > web.txt

python3 showcase_pinecone.py
