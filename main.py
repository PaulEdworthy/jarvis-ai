import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    'gemini-1.5-flash',
    generation_config=genai.GenerationConfig(
        temperature=0.7,
        top_p=1,
        top_k=1,
        max_output_tokens=2048,
    ))

convo = model.start_chat()

# def check_input(user_input):
#     replacements = {
#         "Jays": "Toronto Blue Jays",
#         "Notre Dame": "University of Notre Dame football",
#         "Oilers": "Edmonton Oilers",
#         "Sens": "Ottawa Senators"
#     }
#
#     for old, new in replacements.items():
#         user_input = user_input.replace(old, new)
#         print(user_input)


while True:
    user_input = input("Gemini: ")
    # check to see any keywords in user input and replace them. MAYBE THEY'RE NOT NEEDED?
    # check_input(user_input)
    convo.send_message(user_input)
    print(convo.last.text)
