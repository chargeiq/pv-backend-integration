import uuid



class solar_device:
    def init(self, name, solar_device_id, kwp):
        self._id = uuid.uuid4() # This is the internal ID in couchdb
        self.name = name # This ID can be configured by the user
        self.solar_device_id = solar_device_id # This is the ID 
        self.kwp = kwp

    def set_actual_power(self, power): 
        self.power = power

    def get_actual_power(self, power): 
        return self.power