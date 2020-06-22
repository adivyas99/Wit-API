## Importing libraries-- ##
from wit import Wit
from flask import Flask, render_template, request
import random

## List for random answers
numberList = ['Probably you\'re talking about-', 'I am sure its about - ', 'May be its about - ']

## Creating an Flask app-- ##
app = Flask(__name__)

## Creating Wit Client-- ##
client = Wit('65OUDVOAMYWD32BX3XDXDQJUXPSK7J2F')

## To use the application without Web UI-- ##
## In this case comment the whole block-- ##
'''while True:
    txt_input = input('User: ')
    res = client.message(txt_input)
    #print(res['entities'].keys())
    for i in res['entities'].keys():
        print(random.choice(numberList)+str(i).split(':')[1])'''

## Chatbot Backend-- ##
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    global numberList
    userText = request.args.get('msg')
    res = client.message(userText)
    #print(res['entities'].keys())
    for i in res['entities'].keys():
        answer = random.choice(numberList) + str(i).split(':')[1]
    return answer

## Run the backend ##
if __name__ == "__main__":
    app.run()
    
## Sample sentences- ###
'''Whats the temprature in Austin
How old am I
Transfer $200 to my dad
Go to grocery shopping'''
