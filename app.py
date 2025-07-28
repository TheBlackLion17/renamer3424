# Thank you LazyDeveloper for helping me in this journey!
# Must Subscribe On YouTube @LazyDeveloperr

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '@TheBlackLion17'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # Added host/port for deployment compatibility
