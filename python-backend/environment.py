import datetime
from eif_api.data import Data


class FloorPlan():

    def __init__(self, fireExits, fireSensors):
        self.fireExits = fireExits
        self.fireSensors = fireSensors
        self.hazards = []
        self.totalPeopleOnFloor = 0
        # self.updateTotalPeopleOnFloor()

    def updateTotalPeopleOnFloor(self):
        self.totalPeopleOnFloor = 0

        for exit in self.fireExits:
            exit.updatePeople()
            self.totalPeopleOnFloor = self.totalPeopleOnFloor + (exit.peopleIn - exit.peopleOut)


    def updateHazards(self):
        # Check if existing hazards have been removed
        for hazard in self.hazards:
            if not hazard.fireSensor.isFire():
                self.hazards.remove(hazard)

        for sensor in self.fireSensors:
            if(sensor.isFire()):
                hazard.append(Hazard(sensor.location, sensor))

        # If hazrd on path we need to block corresponding fire exit


class FireExit():

    def __init__(self, peopleUnit, location):
        self.peopleUnit = peopleUnit
        self.blocked = False
        self.location = location
        self.peopleOut = 0
        self.peopleIn = 0

    def updatePeople(self):
        currentTime = datetime.datetime.now() - datetime.timedelta(days=1)
        fiveMinutesAgo = currentTime - datetime.timedelta(minutes=5) - datetime.timedelta(days=1)
        (rc, json) = Data.retrievePersonCount(fiveMinutesAgo, currentTime, self.peopleUnit.family, self.peopleUnit.unit)
        self.peopleOut = json['out']
        self.peopleIn = json['in']
        return (self.peopleOut, self.peopleIn)

class Hazard():

    def __init__(self, location, fireSensor):
        self.location = location
        self.fireSensor = fireSensor


class HazardSensor():

    def __init__(self, sensor, location):
        self.sensor = sensor
        self.location = location

    def isFire(self):
        currentTime = datetime.datetime.now()
        fiveMinutesAgo = currentTime - datetime.timedelta(minutes=5)
        # (rc, json) = Data.retrieve(fiveMinutesAgo, currentTime, self.sensor.family, self.sensor.unit, self.sensor.subCode)

        totalReading = 0
        count = 0
        #for (attr, value) in json.iteritems():
        #    count = count + 1
        #    totalReading = totalReading + value

        #avgTemp = totalReading/count

        #return (avgTemp > 50)
