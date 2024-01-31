import math
from collections import UserDict

DEFAULT_PAGE_SIZE = 10


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record_by_name(self, value):
        for name, record in self.items():
            if name == value:
                return record
        return None

    def page_count(self):
        return math.ceil(len(self.data) / DEFAULT_PAGE_SIZE)

    def iterator(self, page):
        start_offset = page * DEFAULT_PAGE_SIZE
        if start_offset < 0 or start_offset > len(self.data):
            start_offset = 0
        values = list(self.data.values())
        finish_offset = start_offset + DEFAULT_PAGE_SIZE
        if finish_offset > len(values):
            finish_offset = len(values)
        for i in range(start_offset, finish_offset):
            yield values[i]
