from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
import sqlite3
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route('/api/scrape', methods=['GET'])
def get_scraped_data():
    word = request.args.get('word')  # Getting word from the request
    url = "https://www.crawler-test.com"  # Url to scrape
    content = fetch_data(url, word) 

    # Check if some content was found
    if content: 
        # Save scraped data to SQLite
        conn = sqlite3.connect('scraped.db')
        c = conn.cursor()
                # Create table if not exists
        c.execute('CREATE TABLE IF NOT EXISTS ScrapedData (content TEXT, timestamp DATETIME)')
        conn.commit()
        c.execute("INSERT INTO ScrapedData(content, timestamp) VALUES (?, ?)", (content, datetime.now()))

        # Save changes and close connection
        conn.commit()
        conn.close()
        
        # converting data into csv
        pd.DataFrame([content]).to_csv("scraped.csv", index=False)

        return jsonify({"message": "Data scraped and stored successfully", "content": content}), 200
    else:
        return jsonify({"message": "Data not found"}), 404

def fetch_data(url, word):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # Find the word
    try:
        index = text.index(word)

        # Return all text after the word
        return text[index + len(word):]
        
    except ValueError: 
        return None  
def create_database():
    # Connect to SQLite database
    conn = sqlite3.connect('scraped_data.db')
    c = conn.cursor()

    # Create table
    c.execute("CREATE TABLE IF NOT EXISTS ScrapedData (content TEXT, timestamp DATETIME)")

    # Save changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()  # create database and table before running the app
    app.run(debug=True)
