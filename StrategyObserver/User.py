class Observer:
    def update(self, subject):
        pass

class User(Observer):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.suscriptions = []

    # def update(self, subject):
    #    return super().update(subject)
    def get_name(self):
        return self.name

    def update(self, subject):
        print(f"Welcome to {subject.name}, {self.name}")

    def get_money(self):
        return self.money
    
    ###################
    ###################
    def set_money(self, num):
        self.money = num
 
        