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

    def iterator(self, page):
        # page 1 - kontakty od 1 do 10
        # page 2 - kontakty od 11 do 20
        # ...
        # page spoza zakresu - nic
        pass
