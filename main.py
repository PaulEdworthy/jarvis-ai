import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')