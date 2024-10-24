from classes.name import Name
from classes.phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone_number: Phone):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def edit_phone(self, current_phone, new_phone):
        for phone in self.phones:
            if phone.value == current_phone:
                phone.value = new_phone
                break

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
        