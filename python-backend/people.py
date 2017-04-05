from eif_api.data import Data
from eif_api.types import SensorFamily
from eif_api.types import PeopleUnit
import datetime

toDate = datetime.datetime.now() - datetime.timedelta(days=2)
fromDate = toDate - datetime.timedelta(hours=2)

def totalIn(fromDate, toDate):
    (rc, json) = Data.retrievePersonCount(fromDate, toDate, SensorFamily.PEOPLE, PeopleUnit.PC02_15_IN)

    totalIn = 0
    for (attr, value) in json:
        totalIn = totalIn + value

    (rc, json) = Data.retrievePersonCount(fromDate, toDate, SensorFamily.PEOPLE, PeopleUnit.PC02_16_IN)

    for (attr, value) in json:
        totalIn = totalIn + value

    return totalIn

def totalOut(fromDate, toDate):
    (rc, json) = Data.retrievePersonCount(fromDate, toDate, SensorFamily.PEOPLE, PeopleUnit.PC02_15_OUT)

    totalOut = 0
    for (attr, value) in json:
        totalOut = totalOut + value

    (rc, json) = Data.retrievePersonCount(fromDate, toDate, SensorFamily.PEOPLE, PeopleUnit.PC02_16_OUT)

    for (attr, value) in json:
        totalOut = totalOut + value

    return totalOut

def peopleOut(fromDate, toDate, unit):
    (rc, json) = Data.retrievePersonCount(fromDate, toDate, SensorFamily.PEOPLE, unit)

    out = 0
    for (attr, value) in json:
        out = out + value

    return out


exits = [[False, PeopleUnit.PC02_16_OUT], [False, PeopleUnit.PC02_15_OUT]]

totalOut = totalOut(fromDate, toDate)
inB = totalIn(fromDate, toDate)
peopleLeft = (inB - totalOut)

itr = 0
for exit in exits:
    po = peopleOut(fromDate, toDate, exit[1])
    percentLeaving = po / totalOut
    print(exit[1].value + " " + str(percentLeaving))
    if(percentLeaving > 0.65):
        exit[0] = True

for (blocked, unit) in exits:
    print("congeted:" + str(blocked))
