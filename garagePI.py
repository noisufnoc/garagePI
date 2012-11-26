import time
import RPi.GPIO as GPIO
from flask import Flask

app = Flask(__name__)

#setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, True)

@app.route('/')
def root():
    return 'I am working!'

@app.route('/true')
def pin_true():
    GPIO.output(18, True)
    return 'True'

@app.route('/false')
def pin_false():
    GPIO.output(18, False)
    return 'False'

@app.route('/garage')
def garage():
    GPIO.output(18, False)
    time.sleep(1)
    GPIO.output(18, True)
    return 'OPEN ALL THE DOORS\n'

@app.route('/cleanup')
def pin_cleanup():
    GPIO.cleanup()
    return 'All clean'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
