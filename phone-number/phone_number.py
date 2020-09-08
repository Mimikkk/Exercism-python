import re
class PhoneNumber:
    def __init__(self, number: str):
        self.number: str = re.sub(r'[^\d]', '', number)
