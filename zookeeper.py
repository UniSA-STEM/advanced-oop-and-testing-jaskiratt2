from staff import Staff

class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "zookeeper")

    def feed_animal(self, animal):
        return self.get_name() + " will feed " + animal.get_name() + ": " + animal.eat()

    def clean_enclosure(self, enclosure):
        answer = enclosure.clean()
        return self.get_name() + " has cleaned " + enclosure.get_id() + ": " + answer
