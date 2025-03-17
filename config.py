import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API key fron environment variables
# This assumes you have a .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY not set in .env file")