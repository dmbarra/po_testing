import requests
import json
import datetime
import configparser

URL = "/cpi/discovery/v1/catalog/default/browseProductOffering"
FILTER_CATEGORY = "productOffering.category.id.in="
FILTER_NAME = "productOffering.name.in="
JSON_FILE = "../resources/json/browseProductOffering.json"

config = configparser.RawConfigParser()


class BrowsePo:

    def __init__(self, po_name, po_category):
        config.read('../api_address.properties')
        self.payload = "{}"
        self.po_name = po_name
        self.po_category = po_category
        self.load_json_from_file()
        self.create_filter_criteria()
        self.configure_elegibility_date()
        self.result = self.connect_and_request_information()
        self.json_response = json.loads(self.result.text)

    def load_json_from_file(self):
        with open(JSON_FILE) as f:
            self.payload = json.load(f)

    def create_filter_criteria(self):
        self.payload["filterCriterion"] = FILTER_CATEGORY + "[" + self.po_category + "]," + FILTER_NAME + "[" + self.po_name + "]"

    def configure_elegibility_date(self):
        self.payload["eligibilityDate"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    def connect_and_request_information(self):
        headers = {'Content-Type': 'application/json'}
        return requests.post(config.get('CPI', 'address') + URL, json.dumps(self.payload), headers)

    def return_status_code_from_response(self):
        return self.result.status_code

    def return_is_bundle_from_response(self):
        return str(self.json_response['productOfferingQualificationItem'][0]['productOffering']['isBundle'])

    def return_product_specification_from_response(self):
        return self.json_response['productOfferingQualificationItem'][0]['productOffering']['productSpecification']['name']

    def return_po_id_from_response(self):
        return self.json_response['productOfferingQualificationItem'][0]['productOffering']['id']
