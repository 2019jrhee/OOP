import random
class Pokemon(object):

    def __init__(self, name, type, hp):
        self.name = name
        self.hp = hp

        if type == 'fire':
            self.type = {
                'lava': random.randint(20,25),
                'volcano': random.randint(15,20),
                'flaming': random.randint(10,15),
                'magma': random.randint(30,35),
                'heal': random.randint(-35,-30),
                'paralyze': random.randint(10,20)


            }

        elif type == 'water':
            self.type = {
                'waterfall': random.randint(20,30),
                'sprinkler': random.randint(15,20),
                'flood': random.randint(30,40),
                'cycle': random.randint(5,10),
                'heal': random.randint(-35,-30),
                'paralyze': random.randint(10,20)
            }
        #else:
            #print('not a choice')

    def battle(self,enemy):
        for attacks in self.type:
            print(attacks)
        print("%s turn to attack %s"% (self.name, enemy.name))
            # Get user input
        userChoice = input('Which attack do you want to use?')
            # Use user input to apply attack to enemy
        chosen_attack = self.type[userChoice]
        if(self.hp > 1):
            enemy.hp = enemy.hp - chosen_attack
            print("%s did %d damage to %s"%(self.name, chosen_attack, enemy.name ))
            print("%s has %d HP left"%(enemy.name, enemy.hp))
                 # Enemy's turn to attacks
            if (enemy.hp > 1):
                    return enemy.battle(self)
    

        else:
            print ("%s is knocked out. %s won!"%(enemy.name, self.name))
            quit()


Angry = Pokemon('Angry', 'fire', 100)
Cool = Pokemon('Cool', 'water', 100)
Pokemon.battle(Angry,Cool)
