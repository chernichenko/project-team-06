from datetime import datetime

class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d").date()

    def to_str(self):
        return f"{self.name}|{self.address}|{self.phone}|{self.email}|{self.birthday.strftime('%Y-%m-%d')}"

    @staticmethod
    def from_str(data):
        name, address, phone, email, birthday = data.split('|')
        return Contact(name, address, phone, email, birthday)
