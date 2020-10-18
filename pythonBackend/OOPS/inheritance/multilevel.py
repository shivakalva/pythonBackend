class TV:
    name = "Sony HD"

class resolution(TV):
    pixel = 1080

class lookandfeel(resolution):
    def __init__(self):
        self.clarity = "smooth"
        print(" this is {} and good Tv {} and with {}".format(self.clarity, self.pixel, self.name))

my = lookandfeel()
