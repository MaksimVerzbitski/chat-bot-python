from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "Good Times is here. I'm alive!"


def run():
    app.run(host='0.0.0.0', port=8080)

def keep_bot_alive():
    t = Thread(target=run)
    t.start()