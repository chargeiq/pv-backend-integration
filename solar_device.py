import uuid, json



class solar_device:
    def __init__(self, id, name, site_name, solar_device_id, kwp,user_id):
        self._id = id # This is the internal ID in couchdb
        self.name = name # This ID can be configured by the user
        self.site_name = site_name
        self.solar_device_id = solar_device_id # This is the ID 
        self.kwp = kwp # This is the kwp of a solar device
        self.relation = {
            'user_id': user_id
        }

    def set_actual_power(self, power): 
        self.power = power

    def get_actual_power(self, power): 
        return self.power
        
    def serialize(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=4) # , cls = ObjectEncoder, indent=4)
