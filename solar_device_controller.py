import couchdb, json

try:
    couch = couchdb.Server('http://admin:password@192.168.33.113:5984/')

    db = couch.create('solar_device')
except:
    db = couch['solar_device']

def get_solar_device(id):
    pass

def get_solar_device(id):
    pass