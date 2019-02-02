from flask import Flask, jsonify, make_response, request
import os

app = Flask('__name__')

@app.route('/translate/<text>',methods=['GET'])
def tts(text):
    cmd='echo "'+text+'">txt'
    os.system(cmd)
    return jsonify({'message':'request recieved'})

if __name__=='__main__':
    app.run(debug=True)