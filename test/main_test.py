import unittest
import requests
from test.load_csv import LoadDataFile
from test.rest_requests.browse_po import BrowsePo
from ddt import ddt, idata


def po_list():
    load_file = LoadDataFile()
    return load_file.list_of_po()

@ddt
class Test(unittest.TestCase):

    @idata(po_list())
    def test_to_validate_po_configs(self, value):
        self.browsePo = BrowsePo(value[12], value[19])
        self.validate_browse_po_response(value)
        print(value)

    def validate_browse_po_response(self, value):
        assert self.browsePo.return_status_code_from_response() == requests.codes.created
        assert self.browsePo.return_po_id_from_response() is not None
        assert self.browsePo.return_is_bundle_from_response() == value[17]
        assert self.browsePo.return_product_specification_from_response() == value[13]


if __name__ == "__main__":
        unittest.main()