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

    def load_json_from_file(self):
        with open(JSON_FILE) as f:
            self.payload = json.load(f)

    def create_filter_criteria(self):
        self.payload["filterCriterion"] = FILTER_CATEGORY + "[" + self.po_category + "]," + FILTER_NAME + "[" + self.po_name + "]"

    def configure_elegibility_date(self):
        self.payload["eligibilityDate"] = datetime.datetime.now().isoformat()

    def connect_and_request_information(self):
        return requests.post(config.get('CPI', 'address') + URL, self.payload)
