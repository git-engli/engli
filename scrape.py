
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/api/scrape", methods=["GET"])
def get_scraped_data():
    content = fetch_data("https://www.crawler-test.com", "Links")  # replace with the site you want to scrape
    return jsonify(content), 200

def fetch_data(url, word):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()  # get all the text

    # Find the word
    try:
        index = text.index(word)
        # Return all text after the word
        return text[index + len(word):]
    except ValueError: 
        return "The word does not appear in the text"

if __name__ == "__main__":
    app.run(debug=True)

