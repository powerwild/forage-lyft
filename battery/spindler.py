import os
from datetime import datetime
from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self, val):
        self.current_date = val
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + os.environ.get('SPINDLER'))
        return service_threshold_date < datetime.today().date()

    def perform_service(self):
        self.last_service_date = datetime.today.date()
