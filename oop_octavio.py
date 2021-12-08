class Octapus:

    def __init__(self, name='Octavio'):
        self.name = name

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        print("Current name is: ", self.name)


def main():
    zoo_lst = []
    animal_1 = Octapus()
    zoo_lst.append(animal_1)
    animal_2 = Octapus()
    zoo_lst.append(animal_2)
    animal_1.set_name('Oleg')
    animal_1.get_name()
    animal_2.get_name()
    print(len(zoo_lst))


main()
