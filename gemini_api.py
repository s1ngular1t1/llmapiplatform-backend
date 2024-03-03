import textwrap

import google.generativeai as genai
from dotenv import load_dotenv

from IPython.display import Markdown

load_dotenv()

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY= "AIzaSyADRh1wRPX6akSTQkEqLJbNlqECURnfaUI"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def text(prompt):
  model = genai.GenerativeModel('gemini-pro')
  print("This is the request prompt: {}".format(prompt))
  response = model.generate_content(prompt)
  print("the backend server response", response.text)
  to_markdown(response.text)
  return response.text