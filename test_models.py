from models import *


def test_character_name():
    bob_character = Character('bob')
    assert bob_character.first_name == 'bob'


def test_inherits_name():
    alien_bob = Alien()
    assert alien_bob.first_name == 'Xzlty'
    assert alien_bob.planet == 'Earth'


@pytest.mark.parametrize("character, outcome", [
    (Alien(), "The alien aggressively reads poetry at bob!"),
    (Wizard('Dumbledore'), "The wizard drops a heavy book on bob's foot!"),
    (Coder(), "The coder tells bob a dad joke. It's super effective!"),
    (Healer(), "The healer makes bob feel bad for not going to the doctor more frequently")
])
def test_attack(character, outcome):
    bob = Character('bob')
    assert character.attack(bob) == outcome


class TestAlien:
    def test_alien_special_removes_alien_from_party(self):
        alan_the_alien = Alien('Alan')
        bob = Character()
        party = Party([bob, alan_the_alien])
        alan_the_alien.special(party)
        assert party.party_members == [bob]

    def test_alien_only_removes_themselves(self):
        miriam_alien = Alien('Miriam')
        alan_alien = Alien('alan')
        new_party = Party([miriam_alien, alan_alien])
        alan_alien.special(new_party)
        assert new_party.party_members == [miriam_alien]

class TestWizard:
    def test_wizard_special_adds_member_to_party(self):
        anya_the_wizard = Wizard('Anya')
        party = Party([anya_the_wizard])
        alan_the_alien = Alien('Alan')
        anya_the_wizard.special(alan_the_alien)
        assert party.party_members == [anya_the_wizard, alan_the_alien]


class TestCoder:
    """
    The coder's special clones a party member. The new character is included in the party, and their name is the
    reverse of their originator - for example, 'Lucy' would become 'Ycul'. Coders cannot clone Coders!
    """
    def test_coder_special_clones_party_member(self):
        anya_the_coder = Coder("Anya")
        alan_the_alien = Alien("Alan")
        jon_the_wizard = Wizard("Jon")
        party = Party([alan_the_alien, jon_the_wizard])
        anya_the_coder.special(party)
        assert party.party_members == [alan_the_alien, jon_the_wizard, "Nala"] # Could I say alan_the_alien[::-1] ?


    def test_coder_cannot_clone_coder(self):
        anish_the_coder = Coder('Anish')
        antonia_the_coder = Coder('Antonia')
        party = Party([anish_the_coder, antonia_the_coder])
        anish_the_coder.special(party)
        assert len(party.party_members) == 2

class TestTrickster:

        def test_trickster_changes_subclass_to_trickster(self):
            miriam_the_alien = Alien("Miriam")
            tom_the_coder = Coder("Tom")
            jane_the_trickster = Trickster("Jane")
            miriam_the_trickster = Trickster("Miriam")  #After I've changed the subclass should look like this
            party = Party([miriam_the_alien, tom_the_coder, ed_the_wizard])
            jane_the_trickster.special(party)
            assert party.party_members == [miriam_the_trickster, tom_the_coder]
