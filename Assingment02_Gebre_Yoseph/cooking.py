# Source code for Person
class Person:

    def __init_(self, the_last, the_first, the_gender):
        self.last = the_last
        self.first = the_first
        self.gender = the_gender

    def __str__():
        return ("{0:s} {1:s} {3:s}". \
                format(self.last, self.first, self.gender))

    # Source code for Driver


class Driver(Person):

    def __init__(self, the_last, the_first, \
                 the_gender, the_lic_num):
        self.last = the_last
        self.first = the_first
        self.gender = gender
        self.license_number = theLicNum

    def __str__(self):
        return super().str(self) + \
               "{0:s}\n".format(license_number)


drivers = ()
file = open("booklist.txt", 'r')
lines = file.readline()
for ln in lines:

    if len(ln) == 0:
        break
    f = ln.strip(",")
    d = Driver(f[0].strip(), f[1].strip(), f[2].strip, f[3].strip())
    drivers.append(d)

for d in drivers:
    if d.license_number[0] == "N" and d.gender == 'F':
        print("{1:s} {1:s}".format(d.first, d.last))