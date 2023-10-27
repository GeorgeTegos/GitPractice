#Setup Flask , import Flask,jsonify, request
from flask import Flask, jsonify, request

app = Flask(__name__)



# code for routes



if __name__ == '__main__':
    app.run(debug=True)