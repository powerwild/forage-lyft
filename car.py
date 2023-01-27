


class Car():
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self, engine_val, battery_val):
        return self.engine.needs_service(engine_val) or self.battery.needs_service(battery_val)
