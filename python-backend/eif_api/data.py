import requests
import datetime

class Data():
    """Blah."""

    DATE_FORMAT = "%Y-%m-%dT%I:%M:%S"

    @staticmethod
    def livePersonCount(unit):
        """Gets the live person count for that unit."""

        r = requests.get('http://hummingbird.feit.uts.edu.au:8080/peopleCounterApi/live/' + unit.value)

        return (r.status_code, r.json())

    @staticmethod
    def retrievePersonCount(startDate, endDate, family, unit):
        payload = {
            'rFromDate': startDate.strftime(Data.DATE_FORMAT),
            'rToDate': endDate.strftime(Data.DATE_FORMAT),
            'rFamily': family.value,
            'rSensor': unit.value
        }

        r = requests.post('http://eif-research.feit.uts.edu.au/api/json/', params=payload)

        return (r.status_code, r.json())

    @staticmethod
    def retrieve(startDate, endDate, family, unit, subCode):
        """Will get data."""

        payload = {
            'rFromDate': startDate.strftime(Data.DATE_FORMAT),
            'rToDate': endDate.strftime(Data.DATE_FORMAT),
            'rFamily': family.value,
            'rSensor': unit.value,
            'rSubSensor': subCode.value
        }

        r = requests.post('http://eif-research.feit.uts.edu.au/api/json/', params=payload)
        return (r.status_code, r.json())
