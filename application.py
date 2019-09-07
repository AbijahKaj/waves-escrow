import os
import sys

from flask import Flask
from flask import Response
from flask import request
from flask import redirect
from flask import render_template
from flask import jsonify


import requests


import pywaves as pw



# app = Flask(__name__) # to make the app run without any
app = Flask(__name__)



# SERV
@app.route('/', methods=['GET', 'POST'])
def server_work():
    if request.method == 'POST':
        pass
    return render_template('signup.html')

@app.route('/waves', methods=['GET', 'POST'])
def waves():
    if request.method == 'POST':
        pass

    myAddress = pw.Address(privateKey='4GXSoZdGi8bgkC98H8FpNZ5kjv92s8YASRsbNWXU7hVt')
    print(1)
    otherAddress = pw.Address('3NCcsyMn1R9feUBBnFCTBaVcWD2LKq4ErfG')
    print(2)
    myAddress.sendWaves(otherAddress, 10000)
    print(3)
    myToken = myAddress.issueAsset('Token1', 'My Token', 1000, 0)
    print(4)
    while not myToken.status():
        pass
    print(5)
    myAddress.sendAsset(otherAddress, myToken, 50)

    return 'ok'


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp




if __name__ == "__main__":
    app.run(debug=True, port=5000)

