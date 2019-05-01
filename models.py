from typing import List
import copy as cp

class Character(object):
    def __init__(self, name='bob', party: 'Party' = None):
        self.first_name = name
        self.party = party

    def attack(self, target):
        pass

    def special(self, target=None):
        pass

class Party(object):
    def __init__(self, members: List[Character]):  #typehint
        self.party_members = members
        for member in members:
            member.party = self

class Alien(Character):
    def __init__(self, name='Xzlty', planet='Earth'):
        super().__init__(name)
        self.planet = planet

    def attack(self, target):
        return "The alien aggressively reads poetry at {}!".format(target.first_name)

    def special(self, target:Party=None):
        if self in target.party_members:
            target.party_members.remove(self)


class Wizard(Character):
    def __init__(self, name='Dumbledore'):
        super().__init__(name)

    def attack(self, target):
        return "The wizard drops a heavy book on {}'s foot!".format(target.first_name)

    def special(self, target=None):
        target.party = self.party
        self.party.party_members.append(target)  #But which instance of party - needs to corelate with the one from character
                                            #Why reference to part_members unresolved?


class Coder(Character):
    def __init__(self, name='Norman', party=None):
        super().__init__(name, party)

    def attack(self, target):
        return "The coder tells {} a dad joke. It's super effective!".format(target.first_name)

    def special(self, target: Character):
        if isinstance(target, Coder):
            # isinstance function takes two arguments, the thing you want to test and the object to test against
            pass
        else:
            target_copy = self.clone(target)
            target_copy.first_name = self.name_reverser(target_copy.first_name)
            target.party.party_members.append(target_copy)


    def name_reverser(self, name:str):
        return name[::-1].capitalize()

    def clone(self, target:Character):
        return cp.copy(target)


class Healer(Character):
    def __init__(self, name='Doctor'):
        super().__init__(name)

    def attack(self, target):
        return "The healer makes {} feel bad for not going to the doctor more frequently".format(target.first_name)


class Trickster(Character):
    def __init__(self, name, party=None):
        super().__init__(name, party)

    def special(self, target: Character):

        new_trickster = Trickster(target.first_name, target.party)
        target.party.party_members[0] = new_trickster










