import random
import json

def random_quotes():
    with open("quotes.json", "r") as file:
      quotes_file = json.load(file)

    return random.choice(quotes_file)


