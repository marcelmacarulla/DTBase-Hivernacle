from .BaseIngress import BaseIngress
from typing import Tuple, List, Dict #I had to add Tuple

class MinimalExampleDataIngress(BaseIngress):
    # get_service_data is the one method you need to write yourself.
    def get_service_data(self, data: Dict[str, list]) -> List[Tuple[str, dict]]:
        # Create a sensor type.
        return_value: List[Tuple[str, dict]] = [
            (
                "/sensor/insert-sensor-type",
                {
                    "name": "Temperature and humidity sensor",
                    "description": ("A sensor that measures temperature and humidity."),
                    "measures": [
                        {"name": "Temperature", "units": "°C", "datatype": "float"},
                        {"name": "Humidity", "units": "%", "datatype": "float"},
                    ],
                },
            ),
        ]

        # Create a sensor of that type.
        return_value.append(
            (
                "/sensor/insert-sensor",
                {
                    "type_name": "Temperature and humidity sensor",
                    "unique_identifier": "Temperature and humidity sensor #1",
                },
            )
        )

        # Insert readings for the sensor.
        return_value.append(
            (
                "/sensor/insert-sensor-readings",
                {
                    "measure_name": "Temperature",
                    "unique_identifier": "Temperature and humidity sensor #1",
                    "readings": data["temperatures"],
                    "timestamps": data["timestamps"],
                },
            )
        )
        return_value.append(
            (
                "/sensor/insert-sensor-readings",
                {
                    "measure_name": "Humidity",
                    "unique_identifier": "Temperature and humidity sensor #1",
                    "readings": data["humidities"],
                    "timestamps": data["timestamps"],
                },
            )
        )
        print(return_value)
        return return_value