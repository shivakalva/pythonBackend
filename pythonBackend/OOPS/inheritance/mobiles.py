class Samusung:
    Manufacturer = "Samsung inc"
    Contact = "login into www.samsung.com"


class Android(Samusung):
    def __init__(self, model, price):
        self.model = model
        self.price = price


Child = Android('DDDD', 15000)
print(" Details are ", Child.Contact, Child.Manufacturer, Child.Contact, Child.model, Child.price)
