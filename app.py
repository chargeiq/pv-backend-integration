import requests
import time 
from flask import Flask, jsonify, request, Response, render_template, make_response, g
import solar_device

app = Flask(__name__)
api_key = 'L48sslW6ON'

# It comes with example link

def create_solar(site_id):
    pass

def get_solar(site_id):
    solar_device_controller.get_solar_device()

def get_solar_power(site_id):
    end_time = time.localtime( time.time() )
    start_time = time.localtime( time.time()  )
    url = 'https://monitoringapi.solaredge.com/site/'  \
        + site_id + '/power?startTime=' + start_time \
        + '&endTime = ' + end_time
    print(url)
    # requests.get(url)

if __name__ == '__main__': 
    get_solar_power("1")
    app.run(host='0.0.0.0', port= 5001, use_reloader = False) # avoids a loop running twice and flask using two instances. 