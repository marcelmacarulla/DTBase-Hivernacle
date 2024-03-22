from .BaseIngress import BaseIngress
from typing import Tuple, List, Dict #I had to add Tuple

class DTBaseDataIngress(BaseIngress):
    # get_service_data is the one method you need to write yourself.
    def get_service_data(self, data: List[Dict[str, list]]) -> List[Tuple[str, dict]]:
        # Create a sensor type.
        return_value: List[Tuple[str, dict]] = []

        for entry in data:
            return_value.append(
                (
                    "/sensor/insert-sensor-readings",
                    {
                        "measure_name": entry["measure_name"],
                        "unique_identifier": entry["unique_identifier"],
                        "readings": entry["readings"],
                        "timestamps": entry["timestamps"],
                    },
                ),
            )

        print (return_value)
        return return_value