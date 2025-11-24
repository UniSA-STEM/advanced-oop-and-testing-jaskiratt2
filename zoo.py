class Zoo:
    def __init__(self,name):
        self.__name = name
        self.__animal = []
        self.__enclosure = []
        self.__staff = []

    def get_name(self):
        return self.__name

    def add_animal(self,animal):
        self.__animal.append(animal)
    def add_enclosure(self,enclosure):
        self.__enclosure.append(enclosure)
    def add_staff(self,person):
        self.__staff.append(person)

    def get_all_animal(self):
        return self.__animal
    def get_all_enclosure(self):
        return self.__enclosure
    def get_all_staff(self):
        return self.__staff

    def show_zoo_report(self):
        print("!!!" + self.__name + "!!!")
        print("Total Animals:", len(self.__animal))
        print("Total Enclosure:", len(self.__enclosure))
        print("Total Staff:", len(self.__staff))
        print("\n Enclosures")
        for enclosure in self.__enclosure:
            print(enclosure)
        print("\n Zoo Staffs ")
        for person in self.__staff:
            print(person)
