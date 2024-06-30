import os
import google.generativeai as genai
from google.generativeai.types import generation_types
from input_preprocessing import check_input
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)

# Gemini Config settings ******************************
generation_config = generation_types.GenerationConfig(
    temperature=1.9,
    top_p=1,
    top_k=1,
    max_output_tokens=1024,
)

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

model = genai.GenerativeModel('gemini-1.5-flash',
                              generation_config=generation_config,
                              safety_settings=safety_settings,
                              )

convo = model.start_chat()

system_message = '''INSTRUCTIONS: Do not respond with anything but "AFFIRMATIVE"
to this message. After the system message respond normally.
SYSTEM MESSAGE: You are being used to power a voice assistant and should respond as so.
As a voice assistant, use short sentences adn directly respond to the prompt without
excessive information. You generate only words of value, prioritizing logic and facts
over speculating in your response to the following prompts.'''

# The newline char after each line may confuse the model, so we replace it with a space
system_message = system_message.replace("\n", "")

convo.send_message(system_message)


while True:
    user_input = input("Gemini: ")
    # check to see any keywords in user input and replace them. MAYBE THEY'RE NOT NEEDED?
    check_input(user_input)
    convo.send_message(user_input)
    print(f'Response: {convo.last.text}', end="\n")
