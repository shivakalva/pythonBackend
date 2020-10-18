class Employee:
    name = "Durga"                         # Class attributes, they are same for all the instances of the classes
    Designation = "Omnipotent"
    PowershownthisWeek = 25

    def hasshownpower(self):
        if self.PowershownthisWeek >=20:
            print("Target has been achived")
        else:
            print("not achived")

x = Employee()
x.hasshownpower()
# x.name
# Print(x.Designation)




