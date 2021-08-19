import os

my_secret = os.environ['the_pass']

my_secret = os.environ['the_pass']

my_secret = os.environ['the_pass']
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "I am alive father
  
def run():
  app.run(host="0.0.0.0", port=8080)
  
def keep-alive():
  server = Thread(target=run)
  server.start()
  
