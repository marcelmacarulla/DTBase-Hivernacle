from .BaseIngress import BaseIngress
from typing import Tuple, List, Dict #I had to add Tuple

class SendSensors(BaseIngress):
    # get_service_data is the one method you need to write yourself.
    def get_service_data(self, data: Dict[str, list]) -> List[Tuple[str, dict]]:
        # Create a sensor type.
        return_value: List[Tuple[str, dict]] = [
            (
                "/sensor/insert-sensor",
                {
                    "type_name": "Guardian",
                    "unique_identifier": "GMOVE4EDU",
                    "name": "GMOVE4EDU",
                    "notes": "Integrated sensor",
                },
            ),
        ]

        print(return_value)
        return return_value