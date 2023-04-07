import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_geek():
    page_color = os.environ.get('PAGE_COLOR', 'white')  # get the PAGE_COLOR environment variable, default to 'white' if not set
    return f'<h1 style="background-color: {page_color};">Hello from Flask & Docker</h1>'

if __name__ == "__main__":
    app.run(debug=True)

