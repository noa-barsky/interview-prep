class Employee:
    raise_amount = 1.04 #class variables, works for everyone
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = last + first[0] + "@company.com"
    def fullname(self):
        return self.first + " " + self.last
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

noa = Employee("Noa", "Barsky",60000)
print(noa.fullname())
print(noa.first)
noa.apply_raise()
print(noa.pay)
print(noa.__dict__)