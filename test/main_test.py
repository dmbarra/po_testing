import unittest
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
        self.result = self.browsePo.connect_and_request_information()
        print(value)


if __name__ == "__main__":
        unittest.main()