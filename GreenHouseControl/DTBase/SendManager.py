from .SendOnlineDatatoDTBase import ModBusSensors, WeatherSensors, ControlsSensors

class SendOnlineDatatoDTBase:
    """Class that inlcudes 3 types of data to send, data from modbus grid, data from weather
    station and data from controls."""
    def __init__(self):
        self.ModBusSensor=ModBusSensors()
        self.WeatherSensors=WeatherSensors()
        self.ControlsSensor=ControlsSensors()

    def SendModbusData(self, read, date):
        self.ModBusSensor(read, date)

    def SendWeatherData(self, read, date):
        self.WeatherSensors(read, date)

    def SendControlsData(self, read, date):
        self.ControlsSensor(read, date)