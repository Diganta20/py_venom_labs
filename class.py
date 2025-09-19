# class car:
#     bmw = "m3comp"

# german = car()
# print(german.bmw)


class car:
    def __init__(self,name,country):
        self.name = name
        self.country = country

    def bulao(self):
        print(self.country)


bmw =car("m4",'german')

print(bmw.country)
bmw.bulao()