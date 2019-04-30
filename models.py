from typing import List


class Character(object):
    def __init__(self, name='bob'):
        self.first_name = name

    def attack(self, target):
        pass

    def special(self, target=None):
        pass

class Party(object):
    def __init__(self, members: List[Character]):  #typehint
        self.party_members = members

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
        Party.party_members.append(target)  #But which instance of party - needs to corelate with the one from character
                                            #Why reference to part_members unresolved?


class Coder(Character):
    def __init__(self, name='Norman'):
        super().__init__(name)

    def attack(self, target):
        return "The coder tells {} a dad joke. It's super effective!".format(target.first_name)

    def special(self, target:Party=None):
        if isinstance(target.party_members[0], Coder):
            # isinstance function takes two arguments, the thing you want to test and the object to test against
            pass
        else:
            return target.party_members.append(target.party_members[0][::-1].capitalize())

Coder.special(Party([Alien("Miriam"), Wizard("John")]))  # why doesn't this work?

class Healer(Character):
    def __init__(self, name='Doctor'):
        super().__init__(name)

    def attack(self, target):
        return "The healer makes {} feel bad for not going to the doctor more frequently".format(target.first_name)


class Trickster(Character):
    def __init__(self, name):
        super().__init__(name)

    def special(self, target:Party = None):
        target.party_members[0] = Trickster(target.party_members[0].first_name)

Trickster.special(Party([Alien("Miriam"), Wizard("Edward")]))  #Expects type trickster - but I told it to expect Party?







