from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__() #super in this context is a keyword relating to the base class, which in this instance is animal
        self.cold_blooded = True
        self.venom = None
        self.limbs = False

    def _use_tongue_to_smell(self):
        print("Do I say it smells or tastes nice...?")

# sidney = Snake()
#
# sidney.seek_heat()