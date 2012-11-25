import RPi.GPIO as GPIO
from flask import Flask

app = Flask(__name__)

#setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

@app.route('/')
def api_root():
    return 'I am working!'

@app.route('/true')
def api_true():
    GPIO.output(18, True)
    return 'True'

@app.route('/false')
def api_false():
    GPIO.output(18, False)
    return 'False'

@app.route('/open')
def api_open():
    #close circuit
    #wait 2 seconds
    #open circuit
    return 'Open'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
