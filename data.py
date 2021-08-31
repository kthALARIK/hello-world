#
class Pokemon:
    def __init__(self, sublist):
        self.number = int(sublist[0]);
        self.name = sublist[1];
        self.type_1 = sublist[2];
        self.type_2 = self.null_check(sublist[3]);
        self.total = int(sublist[4]);
        self.hp = int(sublist[5]);
        self.attack = int(sublist[6]);
        self.defense = int(sublist[7]);
        self.speed_attack = int(sublist[8]);
        self.speed_defense = int(sublist[9]);
        self.speed = int(sublist[10]);
        self.generation = int(sublist[11]);
        self.legendary = self.bool_fix(sublist[12]);  # add function to change datatyoe into boolean. # boolfix

    # function to check for null - if such, string is demarkated as None.
    def null_check(self, type_2):
        if len(type_2) >= 2:
            output = type_2
        else:
            output = 'None'
        return output

    def bool_fix(self, legendary):
        if 'True' in legendary:
            legendary = True
        else:
            legendary = False
        return legendary

    def __str__(self):
        pokemon_info = '\n' \
                       + '\nNAME: ' + self.name \
                       + '\nNUMBER: ' + str(self.number) \
                       + '\nTYPE 1: ' + self.type_1 \
                       + '\nTYPE 2: ' + self.type_2 \
                       + '\nTOTAL: ' + str(self.total) \
                       + '\nHP: ' + str(self.hp) \
                       + '\nATTACK: ' + str(self.attack) \
                       + '\nDEFENSE: ' + str(self.defense) \
                       + '\nATTACK SPEED: ' + str(self.speed_attack) \
                       + '\nDEFENSE SPEED: ' + str(self.speed_defense) \
                       + '\nSPEED:' + str(self.speed) \
                       + '\nGENERATION: ' + str(self.generation) \
                       + '\nLEGENTARY: ' + str(self.legendary) \
                       + '\n\n'

        return pokemon_info

    def __lt__(self, other):
        if self.total < other:
            bool_check = True
        else:
            bool_check = False
        return bool_check
