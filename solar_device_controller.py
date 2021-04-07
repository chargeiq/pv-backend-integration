import couchdb, json

try:
    couch = couchdb.Server('http://admin:password@192.168.33.113:5984/')

    db = couch.create('solar_device')
except:
    db = couch['solar_device']

#create
def create_device(solar_device):
    print("saving in couchdb")
    db.save(solar_device)
    return("finished")
#read
def get_solar_device(id):
    pass

def test():
    print("testtest")

# update
def update_solar_device(id, solar_device):
    pass

# delete
def create_solar_device(id):
    pass
