import requests
import time, json, datetime
from flask import Flask, jsonify, request, Response, render_template, make_response, g
import solar_device, uuid
import solar_device_controller

from random import * 

app = Flask(__name__)
api_key = 'L48sslW6ON'

# A normed array in relation to kwp, For simulations
kwp_array = [0,0,0,0,0,0.2,0.3,0.4,0.6,0.7,0.9,0.9,1.0,1.0,0.9,0.8,0.6,0.5,0.4,0.3,0.15,0,0,0]

# It comes with example link
@app.route("/update-solaredge-power/<site_id>/<user_id>", methods = ['GET'])
def update_solar_power(site_id):
    # This needs a real solar power api
    end_time = time.localtime(time.time())
    start_time = time.localtime(time.time())
    # TODO: Use real API
    # For other manufactureres this API can be switched to other manufacturers
    # url = 'https://monitoringapi.solaredge.com/site/'  \
    #    + site_id + '/power?startTime=' + str(start_time) \
    #    + '&endTime = ' + str(end_time)

    current_hour = datetime.datetime.now().hour
    print('Current time is: ' + str(current_hour))
    # print(url)
    user_id = "111"
    print(solar_device_controller.get_solar_device(site_id, user_id).serialize())
    current_solar = solar_device_controller.get_solar_device(site_id, user_id).serialize()
    # resp = requests.get(url)
    # print(resp.text)
    
    return "ok"

@app.route("/get-solaredge-station-info/<site_id>", methods = ['GET'])
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
        user_id = "111"
        solar_station = solar_device.solar_device(str(uuid.uuid4()), "1", site_name, site_id, float(peak_power), user_id)
        if solar_device_controller.get_solar_device(site_id, user_id) == None:

            # if solar device already in DB
            solar_device_controller.create_device(solar_station.__dict__)

            resp = make_response(
                jsonify(
                    action = '/get-solaredge-station-info',
                    status = 'OK'
                    )
                )
            return resp 

        else:
            resp = make_response(
                jsonify(
                    action = '/get-solaredge-station-info',
                    status = 'Solar anlage already exists'
                    )
                )
            return resp 

@app.route("/update-solaredge-station-info/<site_id>/<kwp>", methods = ['GET'])
def update_solaredge_station_info(site_id, kwp):
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
        user_id = "111"
        solar_station = solar_device.solar_device(str(uuid.uuid4()), "1", site_name, site_id, float(peak_power), user_id)
        if solar_device_controller.get_solar_device(site_id, user_id) != None:

            # if solar device already in DB
            solar_device_controller.create_device(solar_station.__dict__)

            resp = make_response(
                jsonify(
                    action = '/get-solaredge-station-info',
                    status = 'OK'
                    )
                )
            return resp 
        else:
            
            resp = make_response(
                jsonify(
                    action = '/get-solaredge-station-info',
                    status = 'Solar anlage already exists'
                    )
                )
            return resp     

if __name__ == '__main__': 
    # Import all solars at start


    app.run(host='0.0.0.0', port= 5001, use_reloader = False) # avoids a loop running twice and flask using two instances. 