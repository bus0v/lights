from flask import Flask, request
from fuck import pong, rainbow_cycle

app = Flask(__name__)

@app.route('/pong', methods=['POST'])
def turn_on():
    #call the function
    micro_delay = float(request.form['micro_delay'])
    pong(micro_delay)
    
    return "SUCCESS"

@app.route('/rbw', methods=['POST'])
def turn_off():
    rainbow_cycle(float(request.form['micro_delay']))
    return "SUCCESS"
