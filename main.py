from flask import Flask, Response, render_template
from dotenv import load_dotenv
import os
import waitress

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world!"

waitress.serve(
    app,
    host="127.0.0.1",
    port=os.getenv("SERVE_PORT", "8000"),
)