from collections import UserDict

from classes.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if not self.data.get(record.name.value):
            self.data[record.name.value] = record
            print(f"Contact {record.name.value} added.")
        else:
            print(f"Contact {record.name.value} already exists.")

    def find(self, name: str):
        return self.data.get(name, f'Contact {name} not found.')

    def delete(self, name):
        try:
            self.data.pop(name)
        except KeyError:
            print(f"Contact {name} not found.")
