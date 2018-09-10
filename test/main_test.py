import unittest
import requests
from test.load_csv import LoadDataFile
from test.rest_requests.browse_po import BrowsePo
from test.rest_requests.get_po import GetPo
from ddt import ddt, idata


def po_list():
    load_file = LoadDataFile()
    return load_file.list_of_po()


@ddt
class Test(unittest.TestCase):

    @idata(po_list())
    def test_to_validate_po_configs(self, value):
        self.browse_po = BrowsePo(value[12], value[19])
        self.validate_browse_po_response(value)
        self.get_po = GetPo(self.browse_po.return_po_id_from_response())
        self.validate_get_po_response(value)
        print(value)

    def validate_browse_po_response(self, value):
        assert self.browse_po.return_status_code_from_response() == requests.codes.created
        assert self.browse_po.return_po_id_from_response() is not None
        assert self.browse_po.return_is_bundle_from_response() == value[17]
        assert self.browse_po.return_product_specification_from_response() == value[13]

    def validate_get_po_response(self, value):
        assert self.get_po.return_status_code_from_response() == requests.codes.ok
        assert self.get_po.return_po_id_from_response() == self.browse_po.return_po_id_from_response()
        assert self.get_po.return_is_bundle_from_response() == value[17]
        assert self.get_po.return_product_specification_from_response() == value[13]


if __name__ == "__main__":
    unittest.main()