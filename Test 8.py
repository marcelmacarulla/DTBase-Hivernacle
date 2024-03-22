from GreenHouseControl.DTBase.ModBusSensors import ModBusSensors

M=ModBusSensors()
print(M.types)
M.build_message()
print("send")
M.send_message()


#[('/sensor/insert-sensor-readings', {'measure_name': 'Temperature', 'unique_identifier': 'GMOVE4EDUN', 'readings': [14.27], 'timestamps': ['2023-12-13T13:18:00']})]

