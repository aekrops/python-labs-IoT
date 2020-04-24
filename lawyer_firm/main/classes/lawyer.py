from service import Service


class Lawyer(Service):

    def __init__(self, name, age, price_in_uah, representation_in_court, advice, collecting_evidence):
        super().__init__(representation_in_court, advice, collecting_evidence)
        self.name = name
        self.age = age
        self.price_in_uah = price_in_uah

    def __del__(self):
        return

    def __str__(self):
        name = f'Name: {self.name}\n'
        age = f'Age: {self.age}\n'
        price_in_uah = f'Price: {self.price_in_uah}\n'
        return name + age + price_in_uah + super().__str__()
