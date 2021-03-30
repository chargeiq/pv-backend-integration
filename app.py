import requests
import time, json
from flask import Flask, jsonify, request, Response, render_template, make_response, g
import solar_device #, solar_device_controller

app = Flask(__name__)
api_key = 'L48sslW6ON'

# It comes with example link

def create_solar(site_id):
    pass

def get_solar(site_id):
    solar_device_controller.get_solar_device()

def get_solar_power(site_id):
    # This needs a real solar power api
    end_time = time.localtime( time.time() )
    start_time = time.localtime( time.time()  )
    url = 'https://monitoringapi.solaredge.com/site/'  \
        + site_id + '/power?startTime=' + start_time \
        + '&endTime = ' + end_time
    print(url)
    resp = requests.get(url)

    print(resp.text)

def get_solar_station_info(site_id):
    # TODO: Replace it with real API
    url = 'https://sandbox-api-stg.solaredge.com/solaredge-sandbox-api/site/'  \
        + site_id + '/details?api_key=' + api_key
    print(url)
    resp = requests.get(url)
    
    if resp.status_code == 200:
        print(resp.text)
        req_body = json.loads(resp.text)['details']
        
        site_name = req_body['name']
        print(site_name)
        peak_power = req_body['peakPower']
        location = req_body['location']
        print(peak_power)

    

if __name__ == '__main__': 
    get_solar_station_info("1")
    app.run(host='0.0.0.0', port= 5001, use_reloader = False) # avoids a loop running twice and flask using two instances. 