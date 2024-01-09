#keep_alive.py


from flask import Flask
from threading import Thread
from main import run
import requests
app = Flask("")



@app.route('/')
def home():
  return "I Am Running"


def keep_alive():
  t = Thread(target=run)
  t.start()

keep_alive()
app.run(host='0.0.0.0',port=10000)


