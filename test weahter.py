from GreenHouseControl.DTBase.SendOnlineDatatoDTBase import WeatherSensors

W=WeatherSensors()

date="2024-01-02T00:00:00"

reading = [
    {'ExtTemp': [12],
     'ExtHumidity': [80.1],
     'AtmosPress': [1],
     'WindSpeed': [1],
     'WindSpeed10':[12],
     'WindDir':[2.1],
     'RainInst':[1.1],
     'RainTemp':[1],
     'RainDay':[1.1],
     'RainDayTemp':[1.1],
     'RainMonth':[1.1],
     'RainMonthTemp':[1.1],
     'RainYear':[1.1],
     'RainYearTemp':[1.1],
     'EvapoDay':[1.1],
     'EvapoMonth':[1.1],
     'EvapoYear':[1.1],
     'IndexSolar':[1.1],
     'IndexUV':[1.09],
     'SunSet':['17:00'],
     'SunRise':['18:00'],
    }

]


W.send_message(reading, date)