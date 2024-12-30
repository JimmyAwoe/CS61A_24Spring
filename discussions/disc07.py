# Q1
def draw(hand, positions):
    orderd_positions = positions.sort()
    new_hand = []
    for p in orderd_positions:
        new_hand.append(hand.pop(p))
    return new_hand

# Q2
class Botton:
    def __init__(self, letter, output):
        self.letter = letter
        self.output = output
        self.pressed = 0

    def press(caps_lock):
        self.pressed += 1
        if caps_lock % 2 == 0:
            self.output(self.letter)
            return self.letter
        else:
            self.output(self.letter.upper())
            return self.letter.upper()

class Keyboard:
    def __init___(self, keys, typed):
        self.keys = keys
        self.typed = typed

    def 

        
