from .BaseIngress import BaseIngress
from typing import Tuple, List, Dict #I had to add Tuple

class DTBaseDataIngress(BaseIngress):
    # get_service_data is the one method you need to write yourself.
    def get_service_data(self, data: Dict[str, list]) -> List[Tuple[str, dict]]:
        # Create a sensor type.
        return_value: List[Tuple[str, dict]] = [
            (
                "/sensor/insert-sensor-readings",
                {
                    "measure_name": data["measure_name"],
                    "unique_identifier": data["unique_identifier"],
                    "readings": data["readings"],
                    "timestamps": data["timestamps"],
                },
            ),
        ]
        print (return_value)
        return return_value