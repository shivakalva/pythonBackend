class OperatingSystem:
    multitasking = True
    name = "Realme"

class XT:
    speed = "30 HZ"
    Camera = "32 MP"

class mobile(OperatingSystem, XT):
    def __init__(self):
        if self.multitasking:
            print("This is a multi tasking os.{}".format(self.name))
            print("speed of mobile{} {}".format(self.speed, self.Camera))

moby = mobile()
