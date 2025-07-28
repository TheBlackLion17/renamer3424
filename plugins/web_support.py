# plugins/web_support.py

import os
from flask import Flask
from threading import Thread

# Create Flask web app
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive and running!", 200

# Function to run the web server
def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# Function to start in a separate thread
def web_server():
    t = Thread(target=run)
    t.start()
