import unittest
from test.load_csv import LoadDataFile
from ddt import ddt, idata


def po_list():
    load_file = LoadDataFile()
    return load_file.list_of_po()

@ddt
class Test(unittest.TestCase):

    @idata(po_list())
    def test_to_validate_po_configs(self, value):
        print(value)


if __name__ == "__main__":
        unittest.main()