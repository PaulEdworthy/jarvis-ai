import os
# import pathlib
# import textwrap
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)
# api_secret = os.getenv('API_SECRET')

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("When was Google founded?")

print(response.text)
