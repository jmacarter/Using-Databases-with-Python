# class PartyAnimal:
#     x = 0
#
#     def __init__(self):
#         print "I am constructed"
#
#     def party(self):
#         self.x = self.x + 1
#         print "So far",self.x
#
#     def __del__(self):
#         print "I am destructed", self.x
#
#
# an = PartyAnimal()
#
# an.party()
# an.party()
# an.party()


# print "Type", type(an)
# print "Dir", dir(an)


# class PartyAnimal:
#     x = 0
#     name = ""
#
#     def __init__(self, nam):
#         self.name = nam
#         print self.name,"constructed"
#
#     def party(self):
#         self.x = self.x + 1
#         print self.name, "party count",self.x
#
#
# s = PartyAnimal("Sally")
# s.party()
#
# j = PartyAnimal("Jim")
# j.party()
# s.party()


class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print self.name,"constructed"

    def party(self):
        self.x = self.x + 1
        print self.name, "party count",self.x

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print self.name,"points",self.points

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
