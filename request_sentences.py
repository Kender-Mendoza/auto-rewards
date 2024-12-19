import google.generativeai as genai
from dotenv import load_dotenv
from re import findall
from os import getenv

load_dotenv()

def request_sentences():
  genai.configure(api_key= getenv("API_KEY"))
  model = genai.GenerativeModel(getenv("MODEL"))
  response = model.generate_content(getenv("CONTENT"))
  matches = findall(r'\[([^\]]+)\]', response.text)
  string_cleaned = matches[0].replace('\n', '').replace('"', '').split(',')
  print(repr(string_cleaned))

  return string_cleaned