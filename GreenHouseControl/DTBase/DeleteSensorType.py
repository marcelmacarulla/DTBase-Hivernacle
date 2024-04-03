from .BaseIngress import BaseIngress
from typing import Tuple, List, Dict #I had to add Tuple

class DeleteSensorType(BaseIngress):
    # get_service_data is the one method you need to write yourself.
    def get_service_data(self, data: List[Dict[str, list]]) -> List[Tuple[str, dict]]:
        # Create a sensor type.
        return_value: List[Tuple[str, dict]] = []

        for entry in data:
            return_value.append(
                (
                    "/sensor/delete-sensor-type",
                    {
                        "type_name": entry["type_name"],
                    },
                ),
            )

        print(return_value)
        return return_value