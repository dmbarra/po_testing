import csv

PO_LIST_FILE = '../resources/pos_list.csv'


class LoadDataFile:

    def __init__(self):
        self.reader = []
        self.load_file()

    def list_of_po(self):
        return self.reader

    def load_file(self):
        with open(PO_LIST_FILE, 'r') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                self.append_lines(row)

    def size_of_list(self):
        return len(self.reader)

    def append_lines(self, line):
        if ';;;;;;;;;;;' not in list(line.items())[0]:
            self.create_list_of_list(self.split_the_item(list(line.items())))

    def split_the_item(self, item):
        return ''.join(item[0]).split(";")

    def create_list_of_list(self, item):
        self.reader.append(item[:])
