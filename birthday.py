from datetime import datetime


class Birthday:
    def __init__(self, value):
        self.value = datetime.strptime(value, "%Y-%m-%d")

    def days_to_birthday(self):
        pass
