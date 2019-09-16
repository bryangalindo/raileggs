mport requests
from csx_terminals import terminals_dict
from database import get_containers_by_rail
from constants import csx_url, csx_headers


class CSX:
    def get_containers_dict(self):
        containers_dict = {}
        containers_by_terminal_dict = get_containers_by_rail()
        for k, v in containers_by_terminal_dict.items():
            if 'CSX' in k:
                for container in v:
                    containers_dict.update({container[:-1]: container})
        return containers_dict

    def get_request_payload(self):
        payload = []

        containers_by_terminal_dict = get_containers_by_rail()
        for k, v in containers_by_terminal_dict.items():
            if 'CSX' in k:
                payload_by_terminals = {
                    "terminal": {},
                    "shipmentData": []
                }
                terminal_key = k.split(' - ')[1]
                terminal_payload = terminals_dict[terminal_key]
                payload_by_terminals['terminal'].update(terminal_payload)
                for container in v:
                    shipment_data_template = {
                        "equipmentID": {
                            "equipmentInitial": container[:4],
                            "equipmentNumber": container[4:-1]
                        },
                        "referenceNumber": ''
                    }
                    payload_by_terminals['shipmentData'].append(shipment_data_template)
                payload.append(payload_by_terminals)
        return payload

    def get_tracing_results_list(self):
        payload = self.get_request_payload()
        r = requests.post(csx_url, json=payload, headers=csx_headers)
        return r.json()['shipments']
