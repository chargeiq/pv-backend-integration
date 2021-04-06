import couchdb, json, solar_device

try:
    couch = couchdb.Server('http://admin:password@192.168.33.113:5984/')

    db = couch.create('solar_device')
except:
    db = couch['solar_device']
#create
def create_solar_device(solar_device):
    return db.save(solar_device)

#read
def get_solar_device(id):
    pass


# update
def update_solar_device(id, solar_device):
    pass

# delete
def create_solar_device(id):
    pass
