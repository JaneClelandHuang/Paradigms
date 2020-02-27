from subprocess import call
from Animals import Cow

class Vocalizer:
    def vocalize(self):
        cal(['say',self.name + 'says' + self.sound()])
		
class VocalCow(Vocalizer, Cow):
    pass

c = VocalCow('Bessie')
print(c.speak())    # speak is inherited from cow
c.vocalize()        # vocalize is inherited from vocalizer
