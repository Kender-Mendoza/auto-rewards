import google.generativeai as genai
from dotenv import load_dotenv
from re import findall
from os import getenv
from random import randint

class BuildSentences:
  LANGUAGE = [
    "Spanish",
    "English",
    "Portuguese",
    "French"
  ]

  def __init__(self):
    load_dotenv()
    genai.configure(api_key= getenv("API_KEY"))
    self.model = genai.GenerativeModel(getenv("MODEL"))

  def language(self):
    language_number = len(self.LANGUAGE) - 1
    position_selected = randint(0, language_number)

    return self.LANGUAGE[position_selected]

  def content(self):
    content = "I need one array with fifty different sentences in [language]. " \
              "don't give me the same as always, please and " \
              "I'm using your API for this reason only answer me with the array."

    return content.replace("[language]", self.language())

  def call(self):
    response = self.model.generate_content(self.content())
    matches = findall(r'\[([^\]]+)\]', response.text)
    sentences = matches[0].replace('\n', '').replace('"', '').split(',')

    print("#############")
    print(self.content())
    print("#############")
    print(sentences)
    print("#############")

    return sentences
