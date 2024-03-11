from .BaseIngress import BaseIngress
from typing import Tuple, List, Dict #I had to add Tuple

class SendSensorType(BaseIngress):
    # get_service_data is the one method you need to write yourself.
    def get_service_data(self, data: Dict[str, list]) -> List[Tuple[str, dict]]:
        # Create a sensor type.
        return_value: List[Tuple[str, dict]] = [
            (
                "/sensor/insert-sensor-type",
                {
                    "name": "Guardian",
                    "description": "An integrated sensor to measeure all agricultural parameters.",
                    "measures": [
                        {"name": "Temperature", "units": "°C", "datatype": "float"},
                        {"name": "RelativeHumidity", "units": "%", "datatype": "float"},
                        {"name": "Co2", "units": "ppm", "datatype": "float"},
                        {"name": "Pressure", "units": "kPa", "datatype": "float"},
                        {"name": "ePAR", "units": "µmol m-2 s-1", "datatype": "float"},
                        {"name": "VPD", "units": "kPa", "datatype": "float"},
                        {"name": "DewPoint", "units": "°C", "datatype": "float"},
                        {"name": "FanRPM", "units": "rpm", "datatype": "float"},
                    ],
                },
            ),
        ]


        # Create a sensor of that type.
        return_value.append(
            (
                "/sensor/insert-sensor-type",
                {
                    "name": "SP_522",
                    "description": ("Pyranometer."),
                    "measures": [
                        {"name": "Pyranometer", "units": "W m-2", "datatype": "float"},
                    ],
                },
            ),
        )

        # Create a sensor of that type.
        return_value.append(
            (
                "/sensor/insert-sensor-type",
                {
                    "name": "SQ_618",
                    "description": "ePar",
                    "measures": [
                        {"name": "ePAR", "units": "µmol m-2 s-1", "datatype": "float"},
                    ],
                },
            ),
        )

        print(return_value)
        return return_value