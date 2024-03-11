#Testing the SendData

import GreenHouseControl
#from GreenHouseControl.DTBase.SendData import SendData



# Some made up example data.
data = {
    "measure_name": "Temperature",
    "unique_identifier": "GMOVE4EDU",
    "readings": [10.0, 15.0, 5.0],
    "timestamps": ["2024-01-03T00:00:00", "2024-01-03T00:01:00", "2024-01-03T00:02:00"]
}

send = GreenHouseControl.DTBase.SendData()
send.postData(data)