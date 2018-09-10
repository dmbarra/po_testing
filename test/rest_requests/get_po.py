import requests
import json
import configparser

URL = "/cpi/discovery/v1/catalog/default/productOffering/"
PARAMETER = "?expand=biItem"

config = configparser.RawConfigParser()


class GetPo:

    def __init__(self, po_id):
        config.read('../api_address.properties')
        self.payload = "{}"
        self.po_id = po_id
        self.result = self.connect_and_request_information()
        self.json_response = json.loads(self.result.text)

    def connect_and_request_information(self):
        headers = {'Content-Type': 'application/json'}
        return requests.get(config.get('CPI', 'address') + URL + self.po_id + PARAMETER, headers)

    def return_status_code_from_response(self):
        return self.result.status_code

    def return_is_bundle_from_response(self):
        return str(self.json_response['isBundle'])

    def return_product_specification_from_response(self):
        return self.json_response['productSpecification']['name']

    def return_po_id_from_response(self):
        return self.json_response['id']