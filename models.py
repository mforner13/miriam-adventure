from typing import List


class Character(object):
    def __init__(self, name='bob'):
        self.first_name = name

    def attack(self, target):
        pass

    def special(self, target=None):
        pass


class Alien(Character):
    def __init__(self, name='Xzlty', planet='Earth'):
        super().__init__(name)
        self.planet = planet

    def attack(self, target):
        return "The alien aggressively reads poetry at {}!".format(target.first_name)

    def special(self, target):
        if Alien('Alan') in target:
            return target.remove(Alien('Alan'))
        else:
            pass

    def test_print(self):
        print('Works')


class Wizard(Character):
    def __init__(self, name='Dumbledore'):
        super().__init__(name)

    def attack(self, target):
        return "The wizard drops a heavy book on {}'s foot!".format(target.first_name)


class Coder(Character):
    def __init__(self, name='Norman'):
        super().__init__(name)

    def attack(self, target):
        return "The coder tells {} a dad joke. It's super effective!".format(target.first_name)



class Healer(Character):
    def __init__(self, name='Doctor'):
        super().__init__(name)

    def attack(self, target):
        return "The healer makes {} feel bad for not going to the doctor more frequently".format(target.first_name)


class Party(object):
    def __init__(self, members: List[Character]):  #typehint
        self.party_members = members

test_alien = Alien()

test_alien.test_print()

alien_testing = Alien()

alien_testing.special(Party([Character(), Alien('Alan')]).party_members)


party_list = ['Miriam', 'Forner', 'Jane', 'Tom']

#new_list = list(party_list)


def coder_special(og_list):

    new_list = list(og_list)

    for name in new_list:
        return name[1:]+name[0]  # I'm just returning it not storing it in a list

    og_list.extend(new_list)

    print(og_list)


coder_special(['Miriam', 'Forner', 'Jane', 'Tom'])


"""for name in new_list:
    for letter in name:
        name_list = list(name)
        print(name_list.append(name_list[0]))
        




print(party_list)"""








